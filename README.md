# Bookscan-for-ChatGPT Plus (project)

**Инструкции для проекта ChatGPT по диагностике PDF-книг, восстановлению текстового слоя и созданию удобной навигации.**  
**An instruction-based workflow for inspecting PDF books, repairing text layers, and adding usable navigation in ChatGPT Projects.**

**Instruction set:** `v1.1.0` · **Languages:** Russian (instructions), Russian/English (this README) · **License:** MIT

**GitHub repository:** [Alekcei-BAV/Bookscan-for-ChatGPT-Plus-project-](https://github.com/Alekcei-BAV/Bookscan-for-ChatGPT-Plus-project-)  
**Public repository display name:** `Bookscan-for-ChatGPT Plus (project)`  
**Processing protocol / PDF mark:** `BookScan · v1.1.0` (unchanged).

> **Naming note:** “Plus” is part of the repository name. It is not a claim that this project is an official OpenAI offering or that it requires a ChatGPT Plus subscription. Available file-processing tools and usage limits depend on the user’s ChatGPT environment.

> **Status:** Public instruction set, not a standalone OCR application. Tool availability and output quality depend on the environment. The XMP BookScan passport and tiny page mark are planned by the instructions, but the protocol has not yet been comprehensively validated on a representative PDF test suite. This is an independent community project, **not affiliated with or endorsed by OpenAI**.

## Быстрый старт (Русский)

1. Создайте в ChatGPT проект **BookScan for ChatGPT** (или используйте другое название).
2. Откройте `PROJECT_INSTRUCTIONS.txt`, скопируйте **весь текст** в поле **«Инструкции проекта»**.
3. Добавьте в **источники проекта** **ровно семь файлов**: `00_MAIN.md` — `06_CHANGELOG.md`. Не загружайте туда `README.md`, `LICENSE`, служебные файлы GitHub или книгу в качестве постоянной инструкции.
4. Откройте новый чат **внутри проекта** и приложите PDF-книгу. Первый ответ — **только диагностика** без OCR и изменения исходника.
5. После просмотра плана ответьте **«Начинай»**. Если работа не завершена за один запуск, получите проверенный ZIP с состоянием и ответьте **«Продолжай»**. При отсутствии прежних файлов приложите исходный PDF и последний архив прогресса повторно.
6. Итоговые файлы выдаются **только в проверенном ZIP**, включая PDF и отчёт.

Подробности: [README_FIRST.md](README_FIRST.md) и [главный протокол](00_MAIN.md).

### Основные возможности

- Диагностика до обработки: проверка структуры, существующего текста, шрифтов, XMP-паспорта и навигации **без OCR**.
- Выбор метода по ситуации: сохранить исправный слой → восстановить подтверждённые Unicode-сопоставления → выборочный OCR → полный OCR только при необходимости.
- Иерархические закладки и рабочие ссылки на пунктах **печатного содержания**; две закладки **«Содержание»**, первая и последняя в панели.
- Контрольные точки и возобновление по сохранённому состоянию; защита от повторного применения OCR и ссылок.
- По возможности запись машиночитаемого XMP-паспорта и **одной** маленькой английской метки `BookScan · v1.1.0` на правом краю последней страницы, только после итоговой проверки и при безопасном расположении.
- Проверяемые отчёты: объём работ, выборка проверок, ограничения, финальный SHA-256 внутри отчёта ZIP.
- Предложения по улучшению правил в `PROPOSED_UPDATE.md`, **без самостоятельной правки** источников проекта.

### Важно

**Инструкции — не установленный OCR-движок.** Они не гарантируют доступность Tesseract/OCRmyPDF, бесконечное время выполнения, фоновую обработку или безошибочное распознавание. Метка и паспорт не являются цифровой подписью или независимым сертификатом качества. Публикуйте в этом репозитории **только инструкции и обезличенные технические примеры**, не защищённые авторским правом книги, приватные PDFs, пароли и отчёты с личными данными.

## Quick start (English)

1. Create a ChatGPT **Project**, optionally named **BookScan for ChatGPT**.
2. Paste the complete contents of [`PROJECT_INSTRUCTIONS.txt`](PROJECT_INSTRUCTIONS.txt) into the Project instructions field. **The operational instructions are in Russian**; translation is not yet provided.
3. Add **only** the seven files `00_MAIN.md` through `06_CHANGELOG.md` as Project sources. Keep books out of permanent Project sources.
4. Start a new chat *inside that Project* and attach a PDF book. The first response is **diagnostic only**: no OCR, edits, or completed PDF until you approve the plan.
5. Reply **«Начинай»** (“Start”) to begin, and **«Продолжай»** (“Continue”) to resume from a verified ZIP checkpoint when available. If source files are unavailable in the next chat, reattach the original PDF and the latest progress ZIP.
6. Completed and partial file deliverables arrive **inside verified ZIP archives** only.

The workflow favors retaining valid text over rerunning OCR, adds clickable entries to an existing printed table of contents, and creates hierarchical PDF bookmarks with the first and last bookmarks named **«Содержание»** (“Contents”). It calls for careful validation and an optional XMP BookScan processing passport.

> This repository supplies prompts and workflow requirements, **not executable PDF processing software**. It does not provide an OCR service or guarantee the same tools are available in every ChatGPT environment.

## Repository contents

| Path | Role |
| --- | --- |
| [`PROJECT_INSTRUCTIONS.txt`](PROJECT_INSTRUCTIONS.txt) | Paste into the ChatGPT Project instructions field |
| [`00_MAIN.md`](00_MAIN.md) | Workflow contract and priority rules |
| [`01_DIAGNOSTICS.md`](01_DIAGNOSTICS.md) | First-pass, no-OCR diagnosis |
| [`02_PROCESSING.md`](02_PROCESSING.md) | Repair and OCR strategies |
| [`03_QUALITY_AND_TOC.md`](03_QUALITY_AND_TOC.md) | Quality checks, bookmarks, TOC, BookScan mark |
| [`04_KNOWN_PROBLEMS.md`](04_KNOWN_PROBLEMS.md) | Known defect classes and improvement proposals |
| [`05_PROGRESS_AND_DELIVERY.md`](05_PROGRESS_AND_DELIVERY.md) | Checkpoints, ZIP delivery, XMP passport |
| [`06_CHANGELOG.md`](06_CHANGELOG.md) | Version history and planned regression scenarios |
| [`README_FIRST.md`](README_FIRST.md) | Russian setup and update guide |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to propose changes safely |
| [`tools/validate_and_package.py`](tools/validate_and_package.py) | Standard-library-only structural check and 9-file installation ZIP build |

**For GitHub:** keep the repository source files and optional CI. **For ChatGPT:** install only the `PROJECT_INSTRUCTIONS.txt` text and the seven numbered Markdown files. A downloadable instruction ZIP can be built by running:

```bash
python3 tools/validate_and_package.py --output dist/BookScan_for_ChatGPT_v1.1.0.zip
```

The script validates file presence and selected consistency rules. It does **not** run OCR or prove PDF-processing accuracy.

## Contributing and releases

**Project home:** [GitHub repository](https://github.com/Alekcei-BAV/Bookscan-for-ChatGPT-Plus-project-). To submit an Issue or Pull Request, open the repository and use its GitHub tabs.

Please open an Issue with a **reproducible, redacted technical description** or a Pull Request. Prefer small, tested changes. The project version in the instruction files must remain consistent; record substantive changes in `06_CHANGELOG.md`. The regression scenarios listed there are **plans**, not claims that end-to-end PDF tests already passed.

See [CONTRIBUTING.md](CONTRIBUTING.md). Source code and instructions in this repository are offered under the [MIT License](LICENSE). **Do not commit scanned books or other content you do not have rights to distribute.**
