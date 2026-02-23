/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
    let n = arr.length;
    if (n < 3) return false;

    let i = 0;

    // 1️climb up
    while (i + 1 < n && arr[i] < arr[i + 1]) {
        i++;
    }

    // peak cannot be first or last
    if (i === 0 || i === n - 1) return false;

    // go down
    while (i + 1 < n && arr[i] > arr[i + 1]) {
        i++;
    }

    // must end exactly at last index
    return i === n - 1;
};