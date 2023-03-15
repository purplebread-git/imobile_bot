import emoji

msg = '''14 128 Midnight 🇺🇸  59000
14 128 Midnight 🇮🇳  61800
14 128 Starlight 🇺🇸  59000
14 128 Starlight 🇮🇳  61900
14 128 Red  🇺🇸  59000
14 128 Purple  🇺🇸  59000
14 128 Purple 🇮🇳  61500
14 128 Blue  🇺🇸  59000
  
14 256 Midnight 🇮🇳  74000
14 256 Starlight 🇮🇳  73500
14 256 Purple  🇮🇳  74000
14 256 Blue 🇮🇳  72500'''
price_text = msg
lines = price_text.split('\n')
lines = [x for x in lines if x]
print(lines)
for i in range(0, len(lines)):
    lines[i] = lines[i].split(' ')
    for j in range(0, len(lines[i])):
        if ":" in emoji.demojize(lines[i][j]):
            emoji_flag = lines[i][j]


print(lines)