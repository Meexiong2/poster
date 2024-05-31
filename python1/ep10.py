def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i  # Return the index of the target
    return -1  # Return -1 if the target is not found

def main():
    my_array = [5, 3, 10, 45, 77]
    target = 45
    target2 = 34

    result = linear_search(my_array, target)
    if result != -1:
        print("Element found at index:", result)
    else:
        print("Element not found in the array.")
    
    result2 = linear_search(my_array, target2)
    if result2 != -1:
        print("Element found at index:", result2)
    else:
        print("Element not found in the array.")


main()
