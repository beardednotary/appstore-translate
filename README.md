# appstore-translate
A no-frills Python script that translates your App Store listing into all 37 supported locales and exports a single CSV — ready to copy-paste into App Store Connect.

No API key. No paid service. Just paste your English text and go.

## What It Does
Prompts you for each App Store field, translates into all 37 locales using Google Translate, and saves a app_store_translations.csv you can open in Excel or Google Sheets.

**Fields covered:**

App Name *(30 char limit)*
Subtitle *(30 char limit)*
Description *(4,000 char limit)*
Keywords *(100 char limit)*
What's New *(4,000 char limit)*

**All 37 locales:**
Arabic, Catalan, Chinese (Simplified), Chinese (Traditional), Croatian, Czech, Danish, Dutch, English (Australian), English (Canada), English (UK), Finnish, French, French (Canada), German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Malay, Norwegian, Polish, Portuguese (Brazil), Romanian, Russian, Slovak, Spanish (Mexico), Spanish (Spain), Swedish, Thai, Turkish, Ukrainian, Vietnamese

## Requirements
Python 3.7+ and one dependency:
bashpip install googletrans==4.0.0-rc1

## Usage
bashpython translate_app_store.py
The script will prompt you to paste your English text for each field. Hit Enter twice after each one to confirm. When all fields are done, it translates everything and saves the CSV in the same directory.

## Output
A single app_store_translations.csv with columns:
| locale_name | locale_code | app_name | subtitle | description | keywords | whats_new |
|---|---|---|---|---|---|---|
| French | fr-FR | ... | ... | ... | ... | ... |
| Japanese | ja | ... | ... | ... | ... | ... |

## Notes

**English variants (AU, CA, UK)** copy your source text as-is. Review manually for spelling and phrasing differences.
**French (Canada)** and **Spanish (Mexico)** use the same base translation as French and Spanish (Spain). Flag these for manual review if regional differences matter.
The script warns you in the terminal if any translated field exceeds the App Store character limit.
Uses the free googletrans wrapper — no API key required. A small delay between requests keeps it from getting rate-limited.


## License
MIT — free to use, modify, and share.
