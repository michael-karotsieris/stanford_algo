myComparisons = 0
def partition (A):
    
    pivot = choosePivot(A)
    #print 'The array is ' ,A ,'and pivot chosen to be ' ,A[pivot]
    l = 0
    r = len(A) 
    i = l + 1
    for j in range ( l+1 , r ):
        if A[j] < A[pivot]  :
            swap(A,j,i)         # if element is less tha pivot swap it with i-th
            i += 1              # where i-th element indicates where elements bigger
    swap(A ,pivot, i - 1)      #than the pivot start
    #print 'pivot found its natural position' , A
    left  = A[:i-1]
    right = A[i:]
    return left,right 

def choosePivot(A):
    first  = A[0]
    last = A[-1]
    if len(A)%2 != 0:
        mid = len(A)/2
        middle = A[mid]
    else:
        mid = (len(A)/2) - 1
        middle = A[(len(A)/2) - 1]
    sortedlist = [first,middle,last]
    sortedlist.sort()
    median = sortedlist[1]
    if first == median:
        return 0
    elif last == median:
        return -1
    else:
        return mid
        
def swap(A,first,second):
    temp = A[first]
    A[first] = A[second]
    A[second] = temp

def quicksort(A):
    global myComparisons
    if len(A) == 1:
        return A
    elif len(A)>1:
        left , right = partition(A)
        #print 'left is ', left, 'and right is',right 
        myComparisons = myComparisons + len(A) - 1
        quicksort(left)
        quicksort(right)
        #print myComparisons
        #print left,right
        return A
    else:
        return
      

my_list = []
with open ('QuickSort.txt') as f :
    for number in f:
        my_list.append(int(number))


quicksort(my_list)

    
