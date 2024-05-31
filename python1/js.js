function BinarySearch(array, target) {
    let low = 0;
    let high = array.length - 1;

    while (low <= high) {
        let mid = Math.floor((low + high) / 2);  // Corrected to use integer division
        if (array[mid] === target) {
            return mid;
        } else if (array[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

function Main() {
    let myarray = [3, 4, 5, 6, 7, 10, 56, 77, 88];
    let target = 10;
    // let target2 = 3;

    let result = BinarySearch(myarray, target);
    if (result !== -1) {
        console.log("Element found at index: " + result);
    } else {
        console.log("Element not found in the array.");
    }
}

Main();
