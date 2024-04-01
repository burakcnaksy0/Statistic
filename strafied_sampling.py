import random

from collections import Counter

# Örnek veri seti (meyve ve renk bilgileri)
data = [
    {"meyve": "elma", "renk": "kırmızı"},
    {"meyve": "armut", "renk": "yeşil"},
    {"meyve": "portakal", "renk": "turuncu"},
    {"meyve": "muz", "renk": "sarı"},
    {"meyve": "kivi", "renk": "yeşil"},
]

# Her renk için örneklem büyüklüğü
orneklemler = {"kırmızı": 1, "yeşil": 2, "turuncu": 1}

# Her renk için ayrı ayrı seçin
secilenler = {}
for renk, adet in orneklemler.items():
    secilenler[renk] = [meyve for meyve in data if meyve["renk"] == renk and random.random() < adet / len([meyve for meyve in data if meyve["renk"] == renk])]

# Sonuçları yazdırın
for renk, secilen in secilenler.items():
    print(f"{renk} renk için seçilenler: {secilen}")