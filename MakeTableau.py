''' 4×4 tableau containing the elements.'''
def insert_element(tableau,new_element):
    row = len(tableau)-1
    col = len(tableau[len(tableau)-1])-1
    if tableau[row][col] != float("inf"):
        return 0;
    tableau[row][col] = new_element
    sort(tableau,row,col)
    return 1;


def sort(tableau,i,j):
    row = i
    col = j
    while (i>0 or j>0):
        
        if (i-1)>=0 and tableau[i][j]< tableau[i-1][j]:
            row = i-1
            col = j
            
        if (j-1)>=0 and tableau[row][col]< tableau[i][j-1]:
            row = i
            col = j-1
           
        if row!=i or col!=j:
            temp = tableau[i][j]
            tableau[i][j] = tableau[row][col]
            tableau[row][col] = temp
            i = row
            j = col
        else:
            break;

given_list = [9,16,3,2,4,8,5,14,12]
row = 4
col = 4
tableau = [[float("inf")] * col for i in range(row)]
for i in range(0,len(given_list)):
    result = insert_element(tableau,given_list[i])
print (tableau)
