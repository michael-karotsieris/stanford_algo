import os
def sort_and_count( A , n ):
    #n = len(A)
    if  n==1 :
        return ( A , 0 )
    else:
         B = A[:n/2]
         C = A[n/2:]
         n1 = len( B ) 
         n2 = len( C )
         ( B , x ) = sort_and_count( B , n1 )
         ( C , y ) = sort_and_count( C , n2 )
         ( D , z ) = merge_and_cnt_split( A , B , C , x + y )
    print z 
    return  ( D , z )

def merge_and_cnt_split( A , B , C , cnt ):
    j = 0
    i = 0
    n = len(A)
    l1 = len(B)
    l2 = len(C)
    for k in  range(n) :
        if B[i] < C[j] :
            A[k] = B[i]
            i += 1
            if i >= l1 :
                A[ ( k + 1) : ] = C[j:]
                return ( A , cnt )
                
        else :
            A[k] = C[j]
            j += 1
            cnt += l1 - i
            if j >= l2:
                A[(k + 1):] = B[i:]
                return ( A , cnt )       
    return ( A , cnt )



my_list = []
with open ('integer_array.txt') as f :
    for number in f:
        my_list.append(int(number))

sort_and_count( my_list, len(my_list))




