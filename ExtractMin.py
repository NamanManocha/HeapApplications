''' EXTRACT-MIN on a nonempty m×n Young tableau that runs in O(m+n) time. '''
def extract_min(list_min):
    min_element = list_min[0][0]
    list_min[0][0] = float("inf")
    youngify(list_min,0,0)
    return min_element;

def youngify(list_min,i,j):
    row = i
    col = j

    if (i+1) < len(list_min):
        if list_min[i][j] > list_min[i+1][j]:
            col=j
            row = i+1

    if (j+1) < len(list_min[0]):
        if list_min[row][col] > list_min[i][j+1]:
            col = j+1
            row = i
    
    if(row!=i or col!=j):
        temp = list_min[i][j]
        list_min[i][j] = list_min[row][col]
        list_min[row][col] = temp
        youngify(list_min,row,col)


list_min = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
min_element = extract_min(list_min)
print('Minimum elemet is: ',min_element,'Sorted list',list_min)
    
