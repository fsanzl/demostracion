#!/usr/bin/env python3
from acdh_tei_pyutils.tei import TeiReader, ET
from libEscansion import VerseMetre

filepath = 'text.xml'
xml_file = TeiReader(filepath)
verses = xml_file.any_xpath('.//tei:l')
shared = []
text = ''
for verse in verses:
    if part := verse.xpath('./@part'):
        print(part[0])
        shared.append(verse)
        text += " " + verse.text
        if part[0] == 'F':
            print(text)
            metre = VerseMetre(text).rhythm
            print(metre)
            for partial in shared:
                partial.attrib["met"] = metre
            text = ''
            shared = []
    else:
        text = verse.text
        metre = VerseMetre(text).rhythm
        verse.attrib["met"] = metre
        text = ''
root = xml_file.tree.getroot()
with open(filepath, "wb") as f:
    f.write(ET.tostring(root, pretty_print=True))
