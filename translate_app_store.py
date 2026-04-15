"""
App Store Localization Translator
Translates App Name, Subtitle, Description, Keywords, and What's New
across 37 App Store locales. Outputs a single CSV.

Requirements:
    pip install googletrans==4.0.0-rc1

Usage (PowerShell):
    python translate_app_store.py
"""

import csv
import time
from googletrans import Translator

# ── Locale map: Display name → (App Store locale code, googletrans lang code)
LOCALES = [
    ("Arabic",                "ar-SA", "ar"),
    ("Catalan",               "ca",    "ca"),
    ("Chinese (Simplified)",  "zh-Hans","zh-cn"),
    ("Chinese (Traditional)", "zh-Hant","zh-tw"),
    ("Croatian",              "hr",    "hr"),
    ("Czech",                 "cs",    "cs"),
    ("Danish",                "da",    "da"),
    ("Dutch",                 "nl-NL", "nl"),
    ("English (Australian)",  "en-AU", None),   # same as source, skip translation
    ("English (Canada)",      "en-CA", None),
    ("English (UK)",          "en-GB", None),
    ("Finnish",               "fi",    "fi"),
    ("French",                "fr-FR", "fr"),
    ("French (Canada)",       "fr-CA", "fr"),   # same lang, regional copy
    ("German",                "de-DE", "de"),
    ("Greek",                 "el",    "el"),
    ("Hebrew",                "he",    "iw"),
    ("Hindi",                 "hi",    "hi"),
    ("Hungarian",             "hu",    "hu"),
    ("Indonesian",            "id",    "id"),
    ("Italian",               "it",    "it"),
    ("Japanese",              "ja",    "ja"),
    ("Korean",                "ko",    "ko"),
    ("Malay",                 "ms",    "ms"),
    ("Norwegian",             "no",    "no"),
    ("Polish",                "pl",    "pl"),
    ("Portuguese (Brazil)",   "pt-BR", "pt"),
    ("Romanian",              "ro",    "ro"),
    ("Russian",               "ru",    "ru"),
    ("Slovak",                "sk",    "sk"),
    ("Spanish (Mexico)",      "es-MX", "es"),
    ("Spanish (Spain)",       "es-ES", "es"),
    ("Swedish",               "sv",    "sv"),
    ("Thai",                  "th",    "th"),
    ("Turkish",               "tr",    "tr"),
    ("Ukrainian",             "uk",    "uk"),
    ("Vietnamese",            "vi",    "vi"),
]

FIELDS = [
    ("app_name",    "App Name",    30),
    ("subtitle",    "Subtitle",    30),
    ("description", "Description", 4000),
    ("keywords",    "Keywords",    100),
    ("whats_new",   "What's New",  4000),
]

CHAR_LIMITS = {f[0]: f[2] for f in FIELDS}

def prompt_field(label, char_limit):
    print(f"\n{'─'*60}")
    print(f"  {label}  (English source — limit: {char_limit} chars)")
    print(f"{'─'*60}")
    print("  Paste your text below, then press Enter twice when done:\n")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    text = "\n".join(lines).strip()
    if len(text) > char_limit:
        print(f"  ⚠  WARNING: Text is {len(text)} chars, over the {char_limit}-char limit.")
    return text

def translate_field(translator, text, lang_code):
    """Translate text to lang_code. Returns original text if lang_code is None."""
    if lang_code is None or not text.strip():
        return text
    try:
        result = translator.translate(text, dest=lang_code)
        time.sleep(0.3)  # be polite to the free API
        return result.text
    except Exception as e:
        return f"[ERROR: {e}]"

def warn_length(value, field_key, locale_name):
    limit = CHAR_LIMITS.get(field_key)
    if limit and len(value) > limit:
        print(f"  ⚠  {locale_name} › {field_key}: {len(value)} chars (limit {limit})")

def main():
    print("\n" + "═"*60)
    print("  App Store Localization Translator")
    print("  37 locales → single CSV output")
    print("═"*60)

    # Collect English source text for each field
    source = {}
    for key, label, limit in FIELDS:
        source[key] = prompt_field(label, limit)

    output_file = "app_store_translations.csv"
    translator = Translator()

    print(f"\n\n{'═'*60}")
    print("  Translating... (this may take a minute)")
    print("═"*60)

    fieldnames = ["locale_name", "locale_code"] + [f[0] for f in FIELDS]

    with open(output_file, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for locale_name, locale_code, lang_code in LOCALES:
            print(f"  → {locale_name} ({locale_code})")
            row = {"locale_name": locale_name, "locale_code": locale_code}

            for key, label, _ in FIELDS:
                translated = translate_field(translator, source[key], lang_code)
                warn_length(translated, key, locale_name)
                row[key] = translated

            writer.writerow(row)

    print(f"\n{'═'*60}")
    print(f"  ✓ Done! Saved to: {output_file}")
    print(f"  Open in Excel or Google Sheets.")
    print("═"*60 + "\n")

if __name__ == "__main__":
    main()
