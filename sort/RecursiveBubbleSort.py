def Sort(unsorted_list):
    sorted_list = unsorted_list
    for i in range(len(sorted_list)):
        if i < len(sorted_list)-1 and sorted_list[i] > sorted_list[i+1]:
            sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
            Sort(sorted_list)

    return sorted_list