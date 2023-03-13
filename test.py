a = '''14 128 Midnight 🇺🇸  59000
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
lines = a.split('\n')
print(lines)
lines = [x for x in lines if x]
print(lines)