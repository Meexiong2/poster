def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = low + (high - low) % 2

        if array[mid] == target:
            return mid  # Return the index of the target
        elif array[mid] < target:
            low = mid + 1  # Continue in the upper half
        else:
            high = mid - 1  # Continue in the lower half

    return -1  # Return -1 if the target is not found

def main():
    my_array = [3, 4, 7, 10, 56, 66, 77]
    target = 10
    target2 = 55

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
