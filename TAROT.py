import csv


def citeste_carti(filepath):
    with open(filepath, encoding="utf-8") as f:
        reader=csv.DictReader(f)
        carti=list(reader)
        return carti

carti=citeste_carti("carti_tarot.txt")
print( carti[3])