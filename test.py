a = [['🇺🇸', '13 128 Midnight', 59000], ['🇮🇳', '14 128 Midnight', 61800], ['🇺🇸', '14 128 Starlight', 59000], ['🇮🇳', '14 128 Starlight', 61900], ['🇺🇸', '14 128 Red', 59000], ['🇺🇸', '14 128 Purple', 59000], ['🇮🇳', '14 128 Purple', 61500], ['🇺🇸', '14 128 Blue', 59000], ['🇮🇳', '14 256 Midnight', 74000], ['🇮🇳', '14 256 Starlight', 73500], ['🇮🇳', '14 256 Purple', 74000], ['🇮🇳', '14 256 Blue', 72500]]
print(a)
for i in range(0, len(a)):
    if a[i][0] == "🇺🇸" and int(a[i][1].split(' ')[0]) ==14:
        a[i] = []
a = [x for x in a if x]

print(a)
print(a[0][1].split(' ')[0])