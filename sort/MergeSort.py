def Sort(unsorted_list):
    if (len(unsorted_list) <= 1):
        return unsorted_list

    merge_point = int(len(unsorted_list)/2)

    L = unsorted_list[:merge_point]
    R = unsorted_list[merge_point:]
      
    i=j=k=0
    
    Sort(L)
    Sort(R)

    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            unsorted_list[k] = L[i]
            i=i+1
            k=k+1
        else:
            unsorted_list[k] = R[j]
            j=j+1
            k=k+1
        
    while i < len(L):
        unsorted_list[k] = L[i]
        i=i+1
        k=k+1
    
    while j < len(R):
        unsorted_list[k] = R[j]
        j=j+1
        k=k+1



    return unsorted_list