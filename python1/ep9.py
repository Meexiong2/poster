import bisect

def binary_search(array, target):
    index = bisect.bisect_left(array, target)
    if index < len(array) and array[index] == target:
        return index  # Return the index of the target
    return -1  # Return -1 if the target is not found

def main():
    my_array = [3, 4, 7, 10, 56, 66, 77]
    target = 10
    target2 = 3

    result = binary_search(my_array, target)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found in the array.")
    
    result2 = binary_search(my_array, target2)
    if result2 != -1:
        print("Element found at index:", result2)
    else:
        print("Element not found in the array.")

main()
