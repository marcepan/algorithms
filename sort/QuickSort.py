def Partition(unsorted_list, start_index, end_index):

    if end_index <= start_index:
        return 0

    pivot_index = 0

    j=0

    for i in range(start_index,end_index):

        if unsorted_list[i] < unsorted_list[pivot_index]:
            if i != pivot_index and j!=pivot_index:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j],unsorted_list[i]
            j = j+1

        i=i+1
    
    unsorted_list[pivot_index],unsorted_list[j]=unsorted_list[j],unsorted_list[pivot_index]
    return j

def QuickSort(unsorted_list,start_index,end_index):
    if end_index <= start_index:
        return

    partition_key = Partition(unsorted_list,start_index,end_index)

    QuickSort(unsorted_list,start_index,partition_key)
    QuickSort(unsorted_list,partition_key+1,end_index)

def Sort(unsorted_list):

    QuickSort(unsorted_list,0,len(unsorted_list))

    return unsorted_list





