import sys
def merge(array,left,right):
    i = 0
    j =0
    n = len(array)
    l1 = len(left)
    l2 = len(right)
    for k in range(n):
        print i,j
        if left[i]<right[j]:
            array[k] = left[i]
            i+=1
            if i >= l1 :
                array[i+j:] = right[j:]
                return array
        else:
            array[k] = right[j]
            j+=1
            if j >=  l2:
                array[i+j:] = left[i:]
                return array
    return array
    
def msort(a):
    if len(a)==1:
       return a
    left = a[:len(a)/2]
    right = a[len(a)/2:]
    left = msort(left)
    right = msort(right)
    return merge (a, left ,right)
    


if __name__ == "__main__" :
    print msort([2,7,1,3,8,6,5,9,21,22,4,98,12])
