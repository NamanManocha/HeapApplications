''' insert a new element into a nonfull m×n Young tableau in O(m+n) time. '''

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
        
tableau = [[1,2,3],[4,5,6],[8,9,10],[]]
tableau[3].append(float("inf"))
tableau[3].append(float("inf"))
tableau[3].append(float("inf"))
result = insert_element(tableau,7)
if result == 0:
    print("Tableau is already full")
elif result ==1:
    print("New Element is added in Tableau",tableau)
