#!/usr/bin/python3
import re
from collections import Counter

linefeed = r""""""  # Nueva página
text = ""


def make_line(line):
    line = line.replace("ﬁ", "fi")  # Ligatura ﬁ mal representada
    line = re.sub(linefeed, "|", line)
    line = line.split("|")[-1]
    line = re.sub(r"\s*[\d\s]*\s*$", "", line)  # Más problemas de codificación
    if not re.findall(r"\w", line):
        line = ""
    return line.rstrip()


# Obtiene el tamaño del sangrado de un verso
def spaces_line(line):
    if line.startswith(" "):
        spaces = re.findall(r"^\s*", line)[0]
    elif spaces := re.findall(r"^.*\s{2,}", line):
        spaces = spaces[0]
    else:
        spaces = ""
    return len(spaces)


# Obtiene el tamaño del sangrado regular de los versos
def get_base(page):
    mini = 100
    maxi = 0
    for line in page:
        if sp := re.findall(r"^\S+\s{2,}", line[1]):
            if len(sp[0]) < mini:
                mini = len(sp[0])
    for line in page:
        if current := re.findall(r"^\s{2,}", line[1]):
            if len(current[0]) > maxi:
                maxi = len(current[0])
    if mini < maxi:
        a = mini
    else:
        a = maxi
    return a


def get_base2(page):
    maxi = 0
    for line in page:
        if current := re.findall(r"^\s{2,}", line[1]):
            if len(current[0]) > maxi:
                maxi = len(current[0])
    return maxi


# Normaliza la representación
def parse_spaces(page, ap=False):
    base = get_base(page)
    prev = ""
    text = ""
    for line in page:
        if line[1].startswith(" "):
            if line[0] == base:
                current = f"\t{line[1].strip()}"
            elif line[0] > base:
                current = f"\t\t{line[1].strip()}"
            else:
                current = f"<i>{line[1].strip()}"
        else:
            splitted = line[1].split("  ")
            if len(splitted) > 1:
                character = splitted[0].strip()
                speech = " ".join(splitted[1:]).strip()
            else:
                character = ""
                speech = splitted[0].strip()
            if character:
                text += f"{prev}\n{character.upper()}\n"
                prev = ""
            if line[0] == base:
                current = f"\t{speech}"
            else:
                current = f"\t\t{speech}"
        if re.findall(r"\[.+\]", current):
            aparte = re.findall(r"(.*)(\[.+\])(.*)", current)[0]
            current = aparte[0].rstrip() + aparte[2].lstrip()
            ap = f"\t<i>{aparte[1].strip('[]')}"
            text += f"{ap}\n"
        if current.endswith("]"):
            text += f"{prev} {current.rstrip(']').strip()}\n"
            prev = ""
        elif current.startswith("<i>"):
            if prev.startswith("<i>"):
                prev += " " + current[3:]
            else:
                text += f"{prev}\n"
                prev = current
        else:
            if prev:
                text += f"{prev}\n"
            prev = current
    return f"{text}{prev}\n"


# Lee el archivo de entrada línea a línea
with open("input.txt") as f:
    lines = [line for line in f]

book = []
page = []

# Separa por páginas e indica la líneas y el sangrado
for line in lines:
    if line.startswith(linefeed):
        book.append(page)
        page = []
    if line := make_line(line):
        spaces = spaces_line(line)
        page.append([spaces, line])
book.append(page)

# Normaliza las páginas
for page in book:
    text += parse_spaces(page)
print(text)
