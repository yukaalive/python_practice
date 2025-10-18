prefs = {
    "hokkaido" : "北海道",
    "aomori" : "青森県",
    "iwate" : "岩手県"
}

print(prefs["iwate"])
print(prefs)
print(prefs.keys())
print(prefs.values())
print(prefs.items())

for key in prefs.keys():
    print(key + ":" + prefs[key])