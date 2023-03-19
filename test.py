filter_price_sasha = [['🇮🇳', '14 128 Blue', 63500], ['🇯🇵', '14 Pro 128 Purple', 87000], ['🇯🇵', '14 Pro 256 Purple', 95000]]
percent = 3
print(filter_price_sasha)
for i in range(0, len(filter_price_sasha)):
    filter_price_sasha[i][2] = int(round(((filter_price_sasha[i][2] + int(filter_price_sasha[i][2]*percent/100))/100), 0)*100)

print(filter_price_sasha)

b= 65451
c = int(round(b/100,0)*100)
print(c)