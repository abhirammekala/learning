# In this program the no of items in the array are counted and added to a dictionary

# data = ["red", "green", "red", "red", "red", "red", "green", "red", "green", "green"]
# d = {}
# for i in data:
#     if i in d:
#         d[i] = d[i]+1
#     else:
#         d[i] = 1
# print(d)
data = ["red", "green", "red", "red", "red", "red", "green", "red", "green", "green"]
d = {}
red = 0
green = 0
for i in data:
    if i == "red":
        red = red+1
    elif i == "green":
        green = green+1
d["red"] = red
d["green"] = green
print(d)
