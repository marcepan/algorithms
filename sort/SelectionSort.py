def Sort(unsorted_list):
    sorted_list = unsorted_list
    iterations = len(sorted_list)
    for i in range(iterations):
        min_index = i

        for j in range(i+1, iterations):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
             
        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]

    return sorted_list