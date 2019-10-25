def SortRecursive(unsorted_list, n):
    if n <= 1:
        return unsorted_list
    
    SortRecursive(unsorted_list,n-1)
   

    i = n-1

    while i >= 1 and unsorted_list[i-1] > unsorted_list[i]:
        unsorted_list[i], unsorted_list[i-1] = unsorted_list[i-1], unsorted_list[i]
        i = i-1
    
def Sort(unsorted_list):
    
    SortRecursive(unsorted_list, len(unsorted_list))

    return unsorted_list