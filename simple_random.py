import random

# Örnek veri listesi
data = ["elma", "armut", "portakal", "muz", "kivi"]

# Örneklem büyüklüğü
k = 2

# Rastgele k adet eleman seçin
secilenler = random.sample(data, k)

print("Seçilen örneklem:", secilenler)