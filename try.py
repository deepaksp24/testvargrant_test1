# final code
store = {"leather": {"unit": 1110, "gst": 18, "qua": 1, "t_gst": 0, "bill": 0},
         "umbrella": {"unit": 900, "gst": 12, "qua": 4, "t_gst": 0, "bill": 0},
         "cigaratte": {"unit": 200, "gst": 28, "qua": 3, "t_gst": 0, "bill": 0},
         "honey": {"unit": 100, "gst": 0, "qua": 2, "t_gst": 0, "bill": 0}}
max_gst = 0
max = None

for i in store:
    if store[i]["unit"] > 500:
        store[i]["unit"] -= 0.05 * store[i]["unit"]
for i in store:
    gst = (store[i]['gst']/100)*store[i]["unit"]
    final_gst = gst*store[i]["qua"]
    store[i]["t_gst"] = final_gst
    if max_gst < final_gst:
        max_gst = final_gst
        max = i
print("product with higest gst is", max, "with gst of ", store[max]["t_gst"])
amt = 0
for i in store:
    bill = store[i]["unit"] * store[i]["qua"] + store[i]["t_gst"]
    store[i]["bill"] = bill
    amt += bill
for i in store:
    print(store[i])

print("total amount ", amt)
