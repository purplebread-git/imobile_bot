price_text = """

🇯🇵Apple iPhone SE 128 (2022) Midnight -36.000

🇮🇳Apple iPhone 11 128 White - 44.000

🇮🇳Apple iPhone 12 64 Green - 45.500

🇮🇳Apple iPhone 13 128 Starlight - 56.000
🇮🇳Apple iPhone 13 128 Midnight - 56.000
🇮🇳Apple iPhone 13 128 Blue - 56.000

🇬🇧Apple iPhone 13 256 Blue - 67.000
🇬🇧Apple iPhone 13 256 Midnight - 67.000
🇬🇧Apple iPhone 13 256 Starlight - 67.000

🇦🇪Apple iPhone 14 128 Purple -63.500
🇮🇳Apple iPhone 14 128 Blue -63.500
🇮🇳Apple iPhone 14 128 Midnight -63.500
🇮🇳Apple iPhone 14 128 Starlight -63.500
🇯🇵Apple iPhone 14 128 Red -63.500

🇮🇳Apple iPhone 14 256 Blue -75.000
🇮🇳Apple iPhone 14 256 Midnight -75.000
🇮🇳Apple iPhone 14 256 Starlight -75.000
🇮🇳Apple iPhone 14 256 Purple -76.000

🇨🇦Apple iPhone 14 Plus 128 Red -71.000
🇨🇦Apple iPhone 14 Plus 128 Midnight -73.000

🇯🇵Apple iPhone 14 Pro 128 Gold -85.500
🇯🇵Apple iPhone 14 Pro 128 Silver -88.000
🇯🇵Apple iPhone 14 Pro 128 Purple -87.000
🇪🇺Apple iPhone 14 Pro 128 Black -87.000

🇦🇪Apple iPhone 14 Pro 256 Black -95.500
🇯🇵Apple iPhone 14 Pro 256 Silver -97.500
🇯🇵Apple iPhone 14 Pro 256 Purple -95.000
🇯🇵Apple iPhone 14 Pro 256 Gold -94.500

🇯🇵Apple iPhone 14 Pro 512 Black -118.000
🇸🇬Apple iPhone 14 Pro 512 Purple -118.000
🇯🇵Apple iPhone 14 Pro 512 Silver -117.000

🇨🇦Apple iPhone 14 Pro Max 128 Gold - 94.000
🇪🇺Apple iPhone 14 Pro Max 128 Silver - 96.000
🇯🇵Apple iPhone 14 Pro Max 128 Purple - 96.000
🇯🇵Apple iPhone 14 Pro Max 128 Black - 94.000"""

lines=[]
lines=price_text.split('\n')
c=0
lines = [x for x in lines if x]

for i in range(0,len(lines)):
    lines[i]=lines[i].split(' ', 2)[2]

    lines[i]=lines[i].split(' -',1)
    lines[i][1]=float(lines[i][1].replace(' ',''))
    print(lines[i])
inp=input().split('\n')
print(inp)
for i in range(0,len(lines)):
    if lines[i][0] == inp:
        print('Найдено - ',lines[i])
