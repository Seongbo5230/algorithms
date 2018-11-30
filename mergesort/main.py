import math

def mergesort(array):
    if len(array) > 1:
        # assign arrays into two
        mid = len(array) // 2
        leftArray = array[:mid]
        rightArray = array[mid:]

        mergesort(leftArray)
        mergesort(rightArray)

        # do comparison with left and right arrays, then put into array
        i = j = key = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                array[key] = leftArray[i]
                i += 1
            else:
                array[key] = rightArray[j]
                j += 1
            key += 1

        while i < len(leftArray):
            array[key] = leftArray[i]
            i += 1
            key += 1

        while j < len(rightArray):
            array[key] = rightArray[j]
            j += 1
            key += 1

def main():
    print('Running mergesort')
    array = [5, 2, 4, 7, 1, 3, 2, 6]

    mergesort(array)
    print("Final sorted array: {}".format(array))

if __name__ == "__main__":
    main()
