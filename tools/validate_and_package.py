#!/usr/bin/env python3
"""Check the BookScan instruction sources and build a verified installer ZIP.

Standard library only. This checks package consistency, not OCR/PDF correctness.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
INSTRUCTION_FILES = [
    "00_MAIN.md",
    "01_DIAGNOSTICS.md",
    "02_PROCESSING.md",
    "03_QUALITY_AND_TOC.md",
    "04_KNOWN_PROBLEMS.md",
    "05_PROGRESS_AND_DELIVERY.md",
    "06_CHANGELOG.md",
    "PROJECT_INSTRUCTIONS.txt",
    "README_FIRST.md",
]


def checked_sources() -> tuple[dict[str, bytes], str]:
    contents: dict[str, bytes] = {}
    for name in INSTRUCTION_FILES:
        path = ROOT / name
        if not path.is_file():
            raise ValueError(f"Required file missing: {name}")
        data = path.read_bytes()
        decoded = data.decode("utf-8")
        if len(data) < 100 or "\x00" in decoded:
            raise ValueError(f"Invalid or empty UTF-8 instruction: {name}")
        if decoded.count("```") % 2:
            raise ValueError(f"Unbalanced fenced block in {name}")
        for block in re.findall(r"```json\s*(.*?)\s*```", decoded, flags=re.DOTALL):
            json.loads(block)
        for target in re.findall(r"`(0[0-6]_[A-Z_]+\.md)`", decoded):
            if target not in INSTRUCTION_FILES:
                raise ValueError(f"Broken instruction reference: {name} -> {target}")
        contents[name] = data

    docs = {name: raw.decode("utf-8") for name, raw in contents.items()}
    rx = {
        "00_MAIN.md": r"Версия набора инструкций:\s*(\d+\.\d+\.\d+)",
        "06_CHANGELOG.md": r"Текущая версия:\s*(\d+\.\d+\.\d+)",
        "PROJECT_INSTRUCTIONS.txt": r"Версия правил проекта:\s*(\d+\.\d+\.\d+)",
    }
    versions = {}
    for name, pattern in rx.items():
        match = re.search(pattern, docs[name])
        if match is None:
            raise ValueError(f"No version found in {name}")
        versions[name] = match.group(1)
    if len(set(versions.values())) != 1:
        raise ValueError(f"Conflicting instruction versions: {versions}")
    version = next(iter(versions.values()))

    required_terms = {
        "00_MAIN.md": ["диагностик", "Содержание", "ZIP", "BookScan"],
        "01_DIAGNOSTICS.md": ["без OCR", "XMP", "Начинай"],
        "02_PROCESSING.md": ["ToUnicode", "OCR", "откат"],
        "03_QUALITY_AND_TOC.md": ["первая", "последняя", "CropBox", "#BBBBBB", "BookScan"],
        "05_PROGRESS_AND_DELIVERY.md": ["progress.json", "source_sha256", "final_sha256", "XMP", "ZIP"],
        "PROJECT_INSTRUCTIONS.txt": ["Начинай", "Продолжай", "BookScan", "ZIP"],
    }
    for name, terms in required_terms.items():
        for term in terms:
            if term.casefold() not in docs[name].casefold():
                raise ValueError(f"Expected protocol term missing in {name}: {term}")

    # Assert the small visible mark remains tied to the same rule-set version.
    if f"BookScan · v{version}" not in docs["03_QUALITY_AND_TOC.md"]:
        raise ValueError("BookScan visual mark version differs from instruction version")
    return contents, version


def package(output: Path, sources: dict[str, bytes]) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w") as bundle:
        for name, data in sources.items():
            info = ZipInfo(name, date_time=(2026, 10, 20, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            bundle.writestr(info, data, compress_type=ZIP_DEFLATED, compresslevel=9)
    with ZipFile(output, "r") as bundle:
        if bundle.testzip() is not None:
            raise ValueError("Installer ZIP CRC verification failed")
        if bundle.namelist() != INSTRUCTION_FILES:
            raise ValueError("Installer ZIP has unexpected files")
        for name, original in sources.items():
            if bundle.read(name) != original:
                raise ValueError(f"Archive member differs from repository source: {name}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional path to installable ZIP")
    args = parser.parse_args()
    sources, version = checked_sources()
    print(f"Validated {len(sources)} BookScan instruction files (version {version}).")
    if args.output is not None:
        output = args.output if args.output.is_absolute() else ROOT / args.output
        package(output, sources)
        print(f"ZIP verified: {output} ({output.stat().st_size} bytes)")
        print(f"ZIP SHA-256: {hashlib.sha256(output.read_bytes()).hexdigest()}")
    print("Scope: static consistency checks only; no PDF/OCR testing was performed.")


if __name__ == "__main__":
    main()
