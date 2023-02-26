# implementation of quick sort in python using hoare partition scheme

def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end


if __name__ == '__main__':
    elements = [90, 29, 53, 68, 35, 92, 30, 89, 70, 23]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)

    tests = [
        [90, 29, 53, 68, 35, 92, 30, 89, 70, 23],
        [53, 68, 35, 92],
        [30, 89, 70],
        [23],
        [],
        [90, 29, 53, 68]
    ]

    for elements in tests:
        quick_sort(elements, 0, len(elements)-1)
        print(f'sorted array: {elements}')

