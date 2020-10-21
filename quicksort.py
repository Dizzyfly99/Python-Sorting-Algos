def quicksort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[-1]
    new = [pivot]
    low,high = 0,0
    for i in lst[:-1]:
        if i < pivot:
            new.insert(0,i)
            low += 1
        else:
            new.append(i)
            high += 1
            
    return quicksort(new[:low])+[pivot]+quicksort(new[low+1:])