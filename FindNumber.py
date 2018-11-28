''' O(m+n)-time algorithm to determine whether a given number is stored in a given m×n Young tableau. '''
def search(list_search,element):
    for i in range(0,len(list_search)):
        if list_search[i][0] == element:
            return 1;
        elif list_search[i][0] > element:
            row = i-1
            break;
        else:
            row = i
    
    for j in range(0,len(list_search[0])):
        if list_search[row][j] == element:
            return 1;
    return 0;


list_search = [[1,2,3],[4,5,6],[8,9,10],[11,12,13]]
result = search(list_search,8)
if result == 0:
    print("Element Not Found")
elif result == 1:
    print("Element Found")
