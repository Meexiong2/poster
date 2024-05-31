using System;

class Program
{
    static int BinarySearch(int[] array, int target)
    {
        int low = 0;
        int high = array.Length - 1;

        while (low <= high)
        {
            int mid = low + (high - low) / 2;

            if (array[mid] == target)
                return mid;  // Return the index of the target
            else if (array[mid] < target)
                high = mid - 1;  // Continue in the lower half
            else
                low = mid + 1;  // Continue in the upper half
        }

        return -1;  // Return -1 if the target is not found
    }

    static void Main()
    {
        int[] myArray = { 3,4,7,10,56,66,77 };
        // Array.Sort(myArray);  // Sort the array
        int target = 10;
        int target2 = 3;

        int result = BinarySearch(myArray, target);
        if (result != -1)
            Console.WriteLine("Element found at index: " + result);
        else
            Console.WriteLine("Element not found in the array.");
        
        int result2 = BinarySearch(myArray, target2);
        if (result2 != -1)
            Console.WriteLine("Element found at index: " + result2);
        else
            Console.WriteLine("Element not found in the array.");
    }
}
