function LinearSearch(array, target) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === target)
            return i;  // Return the index of the target
    }
    return -1;  // Return -1 if the target is not found
}

function Main() {
    let myarray = [5, 3, 10, 45, 77];
    let target = 45;
    let target2 = 34;

    let result = LinearSearch(myarray, target);
    if (result !== -1) {
        console.log("Element found at index: " + result);
    } else {
        console.log("Element not found in the array.");
    }

    let result2 = LinearSearch(myarray, target2);
    if (result2 !== -1) {
        console.log("Element found at index: " + result2);
    } else {
        console.log("Element not found in the array.");
    }
}

Main();
