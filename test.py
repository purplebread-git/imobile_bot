lines = ['🇯🇵Apple iPhone SE 128 (2022) Midnight -36.000', '🇮🇳Apple iPhone 11 128 White - 44.000']
for i in range(0, len(lines)):
    vremen_mas = lines[i]

    vremen_mas = vremen_mas.split(' ')[0][0]+vremen_mas.split(' ')[0][1]
    print(vremen_mas)
    lines[i] = lines[i].split(' ', 2)[2]

    lines[i] = lines[i].split(' -', 1)
    lines[i][1] = float(lines[i][1].replace(' ', ''))
    print(lines[i])
