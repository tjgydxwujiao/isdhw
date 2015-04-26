def BinSearch(list,s):
    low = 0
    if list[0] == s:
        return 0

    high = len(list)-1
    while(low < high):
        mid = low + (high - low)//2
        if list[mid]>s:
            high = mid - 1
        elif list[mid] <s:
            low = mid + 1
        else:
            return mid

    if(low == high):
        if(s == list[low]):
            return low
        else:
            return -1
