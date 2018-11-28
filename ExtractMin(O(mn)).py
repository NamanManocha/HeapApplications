''' insert a new element into a nonfull m×n Young tableau in O(m*n) time. '''
def insert_element(list_insert,new_element):
    row = len(list_insert)-1
    col = len(list_insert[len(list_insert)-1])-1
    if list_insert[row][col] != float("inf"):
        return 0;
    list_insert[row][col] = new_element;
    sort(list_insert,row,col)
    return 1;

def sort(list_insert,i,j):
    row = i
    col = j

    if (j-1) >= 0:
        if list_insert[i][j] < list_insert[i][j-1]:
            row = i
            col = j-1
    elif (i-1) >= 0:
        if list_insert[i][j] < list_insert[i-1][len(list_insert[0])-1]:
            row = i-1
            col = len(list_insert[0])-1

    if(row!=i or col!=j):
        temp = list_insert[i][j]
        list_insert[i][j] = list_insert[row][col]
        list_insert[row][col] = temp
        sort(list_insert,row,col)
    



list_insert = [[1,2,3],[4,5,6],[8,9,10],[]]
list_insert[3].append(float("inf"))
list_insert[3].append(float("inf"))
list_insert[3].append(float("inf"))
result = insert_element(list_insert,7)
if result == 0:
    print("Tableau is already full")
elif result ==1:
    print("New Element is added in Tableau",list_insert)
