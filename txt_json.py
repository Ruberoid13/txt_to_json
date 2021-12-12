import json
import csv
import os

r = list()
s = list()
hash = list()

print("Program started.")
os.chdir("C:/Users/ruber/PycharmProjects/txt_to_json")
curpath = os.getcwd()
print("Current dir is ", curpath, sep="")
filename = "res9999.txt"


try:
    print("\nTrying to open ", filename, sep="", end="\n")
    # f = open("C:/Users/ruber/PycharmProjects/txt_to_json/res9999.txt")
    txtfile = open(filename)
except Exception:
    print("Cant open file!")

columns = list(csv.reader(txtfile, delimiter=","))
for i in range(len(columns)):
    columns[i].pop(4)
    columns[i].pop(0)
    r.append(int(columns[i][0], 16))
    s.append(int(columns[i][1], 16))
    hash.append(int(columns[i][2], 16))
    print(r[i], s[i], hash[i])

filename = "data.json"
tuple1 = tuple()
try:
    print("\nTrying to open json ", filename, sep="", end="\n")
    # f = open("C:/Users/ruber/PycharmProjects/txt_to_json/res9999.txt")
    jsonfile = open(filename)
    jsondata = json.load(jsonfile)
except Exception:
    print("Cant open 2 file!")

print(jsondata, "\n", len(jsondata))
print()
dictkeys = list(jsondata.keys())
for i in dictkeys:
    print(i, " = ", jsondata.get(i))
print()
tmp1 = jsondata.get(i)
print("tmp1 = ", tmp1)
tmp1_keys = list(tmp1[0].keys())
print("tmp1_keys = ", tmp1_keys)

r1 = list()
s1 = list()
hash1 = list()

for c in tmp1:
    for i in tmp1_keys:
        val = c.get(i)
        print("value by key \"", i, "\" = ", val, sep="")
        if i == "r":
            r1.append(val)
        if i == "s":
            s1.append(val)
        if i == "hash":
            hash1.append(val)
    print()
for i in range(len(r1)):
    print(r1[i], s1[i], hash1[i])

# for c in range(len(r)):
#     newsig.update(list(newsig.keys()[0]), r[c])
#     print()

# print(json.dumps(f, sort_keys=True, indent=4))
# print(jsonfile.read())

