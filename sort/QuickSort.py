def Sort(unsorted_list):
    
    if len(unsorted_list) <=1:
        return unsorted_list

    pivot_index = 0
    
    i=j=0
    
    for i in range(len(unsorted_list)-1):

        if unsorted_list[i] <= unsorted_list[pivot_index]:
            unsorted_list[i], unsorted_list[j] = unsorted_list[j],unsorted_list[i]
            j = j+1
            
        i=i+1
    unsorted_list[pivot_index],unsorted_list[j]=unsorted_list[j],unsorted_list[pivot_index]

    Sort(unsorted_list[:j])
    Sort(unsorted_list[j-1:])

    return unsorted_list

    



