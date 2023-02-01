#!/usr/bin/env python

import argparse

consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWZ"
vowels = "aeiouyåäöAEIOUYÅÄÖ"
string = "Vad kul Python programmering är"
rovarstring = "VoVadod kokulol PoPytothohonon poprorogogroramommomerorinongog äror"


# Stjärnspråket: en stjärna läggs till efter varje bokstav.
# "Stjärna" blir S*t*j*ä*r*n*a.
# Här har vi dock ändrat koden litet till en modul rubrik.
def stjarnsprak(lanuage):
    print("".join(
        l + '*'  # Lägg till en stjärna efter aktuell bokstav.
        # Kolla om aktuell bokstav är med i våra definierade strängar...
        if l in consonants
        or l in vowels
        else l  # Annars ersätter vi med ett frågettecken.
        for l in lanuage))


# Viskspråket: alla vokaler tas bort.
# Om man matar in "kor" blir det k + ' ' + r  = "k r".
def visksprak(lanuage):
    print("Viskspråket: " + "".join(
        ' '  # Mellanslag ersätter aktuell vokal.
        if l in vowels  # Kolla om aktuell bokstav är en vokal.
        else l  # Annars lägg bara till akuell bokstav till den nya strängen.
        for l in lanuage)  # Loopa igenom alla inmatade bokstäver och gör ovan tills texten är slut.
        + "\n")


# Rövarspråket: alla konsonanter fördubblas och 'o' stoppas in emellan.
# "kor" blir  k + (o + k) + o + r + (o + r) = "kokoror".
def rovarsprak(lanuage):
    print("".join(
        # Lägg till o efter aktuell bokstav och lägg even till en kopia av bokstaven efter o.
        l + 'o' + l
        if l in consonants  # Kolla om aktuell bokstav är en konsonant.
        else l  # Annars lägg bara till akuell bokstav till den nya strängen.
        for l in lanuage)  # Loopa igenom alla inmatade bokstäver och gör ovan tills texten är slut.
        + "\n")


# Rövarspråket: alla konsonanter fördubblas och 'o' stoppas in emellan.
# Denna funktion där bort vokalen och dubbletten av varje funnen konsonant, vid varje loop.
def svenskarovarsprak(language):
    # translation = ""
    for i in range(0, len(language)):
        if i < len(language) and language[i] in consonants:
            language = language[:i] + language[i + 2:]
    # translation = language[:i + 1]
    # range tar hela aktuella input strängen. Strängen förkortas genom slice.
    # Vi ser först till att undvika string index out of range error genom att se till att i är
    # mindre än aktuella inputsträngens längd. Sedan kollar vi om det är en konsonant.
    # Sen gör vi en slice för att ta med alla tecken från början av inkommande rövarspråkssträng, fram till och med i.
    # Vi gör en ny slice för att bli av med en vokal och följande konsonant.
    # Vi sätter sen ihop rövarspråksträngen ingen, nu med minskad längd vilket påverkar
    # range i for loopen. Vi behöver inte translation variabeln men den kan användas under debugging
    # för att se hur itereringen fungerar.

    print("Översättning till Svenska från Rövarspråket: " + language + "\n")


# Bebisar säger bara första stavelsen i varje ord men de säger den tre gånger:
# En stavelse är alla tecken i ett ord fram till och med första vokalen.
def bebissprak(language):
    translation = ""
    cut_letters = ""
    for l in language.split():
        for i in range(0, len(l)):
            if i < len(l) and l[i] in vowels:
                cut_letters = l[:i + 1] * 3
                translation += cut_letters + " "
                break
    print("Bebisspråket: " + translation + "\n")


# För varje ord: bokstäverna före första vokalen sätts sist och "all" läggs till på slutet.
def allspraket(language):
    translation = ""
    cut_consonants = ""
    all = "all"
    for l in language.split():
        for i in range(0, len(l)):
            if i < len(l) and l[i] in vowels:
                cut_consonants = l[:i]
                translation += l[i:] + cut_consonants + all + " "
                break

    print("Allspråket: " + translation + "\n")


# Ordet kuperas som i allspråket fast efter första vokalen. "fi" sätts först och "kon" sist.
def fikonspraket(language):
    translation = ""
    cut_letters = ""
    fi = "fi"
    kon = "kon"
    for l in language.split():
        for i in range(0, len(l)):
            if i < len(l) and l[i] in vowels:
                cut_letters = l[:i + 1]
                translation += fi + l[i + 1:] + cut_letters + kon + " "
                break
    print("Fikonspråket: " + translation + "\n")


def bash(file, sprak):
    translation = ""

    with open(file) as filein:
        for line in filein:
            translation += line

    if sprak == "ST":
        stjarnsprak(translation)
    elif sprak == "R":
        rovarsprak(translation)
    elif sprak == "S":
        svenskarovarsprak(translation)
    elif sprak == "B":
        bebissprak(translation)
    elif sprak == "A":
        allspraket(translation)
    elif sprak == "F":
        fikonspraket(translation)
    elif sprak == "V":
        visksprak(translation)


def main():
    # Lägger till args
    parser = argparse.ArgumentParser(description="Odd Languages")
    parser.add_argument(
        "file", help="Choose a file for translation: --file FILE", type=str)
    parser.add_argument("--st", help="Star Language --st ST", type=str)
    parser.add_argument("--r", help="Robber's language --r R", type=str)
    parser.add_argument("--s", help="Robber's To Swedish --s S", type=str)
    parser.add_argument("--b", help="Baby Language --b B", type=str)
    parser.add_argument("--a", help="All Language --a A", type=str)
    parser.add_argument("--f", help="Fig Language --f F", type=str)
    parser.add_argument("--v", help="Whisper Language --v V", type=str)
    parser.add_argument("--lang", help="Choose language for one line translation: St Ro Sv Be Al Fi LANG\n" +
                        " WHEN YOU USE ECHO: echo |.filename.py 'text to be translated' --spraak 'Ro' ")
    args = parser.parse_args()

    # Filöversättning
    if args.file != "":
        file = args.file
    if args.st == "ST":
        bash(file, "ST")
    if args.r == "R":
        bash(file, "R")
    if args.s == "S":
        bash(file, "S")
    if args.b == "B":
        bash(file, "B")
    if args.a == "A":
        bash(file, "A")
    if args.f == "F":
        bash(file, "F")
    if args.v == "V":
        bash(file, "V")

    # En rads översättning
    if args.lang == "St":
        stjarnsprak(file)
    if args.lang == "Ro":
        rovarsprak(file)
    if args.lang == "Sv":
        svenskarovarsprak(file)
    if args.lang == "Be":
        bebissprak(file)
    if args.lang == "Al":
        allspraket(file)
    if args.lang == "Fi":
        fikonspraket(file)
    if args.lang == "Vi":
        visksprak(file)


if __name__ == '__main__':
    main()
