def Sort(unsorted_list):
    sorted_list = unsorted_list
    iterations = len(sorted_list)
    isSorted = False
    while (not isSorted):
        isSorted = True
        for i in range(iterations):
            
            if i < iterations-1 and sorted_list[i]>sorted_list[i+1]:
                sorted_list[i],sorted_list[i+1]=sorted_list[i+1],sorted_list[i]
                isSorted = False
                       
    return sorted_list