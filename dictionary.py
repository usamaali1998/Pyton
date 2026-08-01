#dictionary = a collection of {key: value} pairs orderedd and changeable. No duplicates

capitals = {"USA":"Washington D.C",
            "Pakistan": "ISlamabad",
            "China": "Beijing",
            "Russia": "Moscow"}
#print(capitals.get("USA"))

#if capitals.get("Pakistan"):
#    print("The capital exists")
#else:
#    print("The capital does not exist")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Newyork"})
capitals.pop("Russia")
#popitem will delete the latest pair

#capitals.popitem()
#clear() will clear the dictionary
#capitals.clear()

#keys() will show all the keys
print(capitals.keys())
print(capitals)

#we can use for loop

for key in capitals.keys():
    print(key)

#same like keys we have a value method as well
values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

#we can also use item() to show the both key value
items = capitals.items()
print(items)


for key,value in capitals.items():
    print(f"{key}:{value}")
