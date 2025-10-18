areas = {
    "hokkaido":["北海道"],
    "tohoku":["青森県", "岩手県", "宮城県"]

}

for area in areas.keys():
    #print(area)
    for pref in areas[area]:
        print(pref)
    print("==")