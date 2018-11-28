''' n×n Young tableau to sort n2 numbers in O(n3) time. '''
import ExtractMin
import NewElement

given_list = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
list_sorted = []
row = 4
col = 4
tableau = [[float("inf")] * col for i in range(row)]
for i in range(0,(row*col)):
    NewElement.insert_element(tableau,given_list[i])

for i in range(0,(row*col)):
    list_sorted.append(ExtractMin.extract_min(tableau))
print("Sorted list is :",list_sorted)
