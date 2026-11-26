#!/usr/bin/env python3
import argparse
import sys

CONSONANTS = set("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
VOWELS = set("aeiouyåäöAEIOUYÅÄÖ")


def stjarnsprak(text: str) -> str:
    """Lägger till '*' mellan bokstäver i varje ord: 'Stjärna' -> 'S*t*j*ä*r*n*a'."""
    words = text.split(" ")
    result = []
    for word in words:
        letters = [c for c in word if c in CONSONANTS or c in VOWELS]
        # Om ordet bara består av bokstäver läggs '*' enbart mellan dem
        if len(letters) == len(word) and len(word) > 1:
            result.append("*".join(word))
        else:
            result.append(word)
    return " ".join(result)


def visksprak(text: str) -> str:
    """Ersätter alla vokaler med mellanslag: 'kor' -> 'k r'."""
    return "".join(" " if c in VOWELS else c for c in text)


def rovarsprak(text: str) -> str:
    """Fördubblar konsonanter med ett 'o' emellan: 'kor' -> 'kokoror'."""
    return "".join(f"{c}o{c}" if c in CONSONANTS else c for c in text)


def svenskarovarsprak(text: str) -> str:
    """Översätter tillbaka från rövarspråket till svenska."""
    result = []
    i = 0
    while i < len(text):
        result.append(text[i])
        if (
            text[i] in CONSONANTS
            and i + 2 < len(text)
            and text[i + 1].lower() == "o"
            and text[i + 2].lower() == text[i].lower()
        ):
            i += 3
        else:
            i += 1
    return "".join(result)


def bebissprak(text: str) -> str:
    """Upprepar första stavelsen (fram till första vokalen) tre gånger."""
    result = []
    for word in text.split():
        for i, c in enumerate(word):
            if c in VOWELS:
                result.append(word[: i + 1] * 3)
                break
        else:
            result.append(word)  # Behåll ord som helt saknar vokaler
    return " ".join(result)


def allspraket(text: str) -> str:
    """Flyttar konsonanter före första vokalen till slutet och lägger till 'all'."""
    result = []
    for word in text.split():
        for i, c in enumerate(word):
            if c in VOWELS:
                result.append(f"{word[i:]}{word[:i]}all")
                break
        else:
            result.append(f"{word}all")
    return " ".join(result)


def fikonspraket(text: str) -> str:
    """Delar ordet efter första vokalen, sätter 'fi' först och 'kon' sist."""
    result = []
    for word in text.split():
        for i, c in enumerate(word):
            if c in VOWELS:
                result.append(f"fi{word[i + 1:]}{word[: i + 1]}kon")
                break
        else:
            result.append(f"fi{word}kon")
    return " ".join(result)


LANGUAGES = {
    "st": ("Stjärnspråket", stjarnsprak),
    "vi": ("Viskspråket", visksprak),
    "ro": ("Rövarspråket", rovarsprak),
    "sv": ("Svenska från Rövarspråket", svenskarovarsprak),
    "be": ("Bebisspråket", bebissprak),
    "al": ("Allspråket", allspraket),
    "fi": ("Fikonspråket", fikonspraket),
}


def main():
    parser = argparse.ArgumentParser(
        description="Översätt text, filer eller stdin till svenska lekspråk."
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="Text att översätta (om varken --file eller pipe används).",
    )
    parser.add_argument(
        "-f", "--file", help="Sökväg till en textfil att översätta."
    )
    parser.add_argument(
        "-l",
        "--lang",
        choices=LANGUAGES.keys(),
        required=True,
        help="Målspråk: st (stjärn), vi (visk), ro (rövar), sv (från rövar), be (bebis), al (all), fi (fikon).",
    )
    args = parser.parse_args()

    # Hämta indata från fil, direkt argument eller stdin (pipe)
    if args.file:
        try:
            with open(args.file, encoding="utf-8") as f:
                input_text = f.read()
        except FileNotFoundError:
            sys.exit(f"Fel: Filen '{args.file}' hittades inte.")
    elif args.text:
        input_text = args.text
    elif not sys.stdin.isatty():
        input_text = sys.stdin.read().strip()
    else:
        parser.error("Du måste ange en text, en fil (--file) eller skicka in text via pipe.")

    lang_name, func = LANGUAGES[args.lang]
    print(f"{lang_name}: {func(input_text)}")


if __name__ == "__main__":
    main()
