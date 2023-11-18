arr = [["leather", 1110, 18, 1],
       ["umberlla", 900, 12, 4],
       ["cigarette", 200, 28, 3],
       ["honey", 100, 0, 2]]
size = len(arr)
max_gst = 0
max_gst_item = 0
arr_gst = [0 for i in range(size)]
for i in range(size):
    gst = (arr[i][2]/100)*arr[i][1]
    final_gst = gst*arr[0][3]
    arr_gst[i] = final_gst
    print(final_gst)
    if max_gst < final_gst:
        max_gst = final_gst
        max_gst_item = i

print("product with highest GST is", arr[max_gst_item][0])
print("GST is", max_gst)
print(arr_gst)

final_bill = 0
for j in range(size):
    amt = arr[j][1]*arr[j][3] + arr_gst[j]
    final_bill += amt

print("final bill of all items is ", final_bill)
if final_bill > 500:
    dis = 0.05 * final_bill
    final_bill -= dis
    print("final bill after 5% of discount", final_bill)
# for i in range(size):

# gst = (arr[0][2]/100)*arr[0][1]
# final_gst = gst*arr[0][3]
# print(gst)
# print(final_gst)
# print(size)
