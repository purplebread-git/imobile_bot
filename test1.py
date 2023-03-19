a = [['🇦🇪', '14 128 Purple', 63500], ['🇮🇳', '14 128 Blue', 63500], ['🇮🇳', '14 256 Purple', 76000],
     ['🇯🇵', '14 Pro 128 Purple', 87000], ['🇯🇵', '14 Pro 256 Purple', 95000]]
b = [['🇺🇸', '14 128 Purple', 59000], ['🇮🇳', '14 128 Purple', 61500], ['🇺🇸', '14 128 Blue', 59000],
     ['🇮🇳', '14 256 Purple', 74000]]

def filter_price(a, b):
    a_processed = []
    b_processed = []

    for el_a in a:
        for el_b in b:
            if el_a[1] == el_b[1]:
                if el_a[2] < el_b[2]:
                    a_processed.append(el_a)
                elif el_b[2] < el_a[2]:
                    b_processed.append(el_b)
                break
        else:
            a_processed.append(el_a)

    for el_b in b:
        for el_a in a:
            if el_b[1] == el_a[1]:
                break
        else:
            b_processed.append(el_b)
    return a_processed, b_processed

fil = filter_price(a,b)
print(fil[0])
print(fil[1])