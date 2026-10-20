# Contributing to BookScan for ChatGPT

Contributions are welcome. This is an independent instruction-based workflow for ChatGPT Projects, **not a production OCR program**.

**Repository:** [https://github.com/Alekcei-BAV/Bookscan-for-ChatGPT-Plus-project-](https://github.com/Alekcei-BAV/Bookscan-for-ChatGPT-Plus-project-).

## Proposing changes

1. Open an Issue describing the symptom, expected behavior, actual behavior, and affected instruction file. If relevant, include **redacted** tool versions, page counts, anonymized PDF structure, and clear reproduction steps.
2. Explain why a change is needed and what observations support it. Separate tested fixes from hypotheses and proposed experiments.
3. If possible, submit a focused Pull Request that updates the relevant rule(s). Keep `00_MAIN.md` authoritative and preserve the first-upload diagnostic-only rule, ZIP-only delivery, and double **«Содержание»** bookmark convention unless proposing a clearly identified protocol change.
4. Include test notes, limitations, and any necessary changelog/version update. The repository's validator provides **structural checks only**, not a guarantee of PDF correctness.
5. Maintainers decide whether to accept the suggestion into the permanent instructions. A GitHub Issue alone does not update an existing ChatGPT Project's uploaded sources.

## Privacy and copyrights

**Never upload copyrighted books, whole PDF pages, private PDFs, passwords, access tokens, personal information, or unredacted reports without suitable permission.** Provide minimal synthetic or independently shareable examples. Remove metadata and identifiers from screenshots or logs. Do not assume a document uploaded to ChatGPT is licensed for GitHub redistribution.

## Versions

- Keep the instruction-set version synchronized across `00_MAIN.md`, `06_CHANGELOG.md`, and `PROJECT_INSTRUCTIONS.txt`.
- `PATCH`: correction without new behavior; `MINOR`: compatible new capability; `MAJOR`: incompatible workflow change.
- Specify whether BookScan XMP/mark and navigation changes were *actually tested* on representative PDFs; never infer tests from the text of an instruction.

## License

By submitting a contribution, you agree it will be distributed under this repository's MIT License.
