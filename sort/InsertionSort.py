def Sort(unsorted_list):
    for i in range(1, len(unsorted_list)):

        while i > 0 and unsorted_list[i] < unsorted_list[i-1]:
            
            unsorted_list[i], unsorted_list[i-1] = unsorted_list[i-1], unsorted_list[i]

            i = i-1      
            
    return unsorted_list
