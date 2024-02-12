"""
Problem Statement:- 
    An array will be given which contains elements in an ascending order.
    return an output array which contains squared elements of the input array
    without modifying it.

    Note: Input array also contains negative elements.

"""


def sortedSquaredArray(array):
    """
        Approach 1: | Time Complexity: O(Nlog(N)) | Space Complexity: O(N).

        Iterate over the array and as you are iterating square the element and insert
        it in empty array which we initialsed before started iterating and sort
        the array using built-in python function

        array.sort()

        then return the output array which contains squared elements of input array.

    _________________________________________________________________________________________

        Approach 2: Time Complexity: O(N) | Space complexity: O(N)

        Initialise an Empty array as for the previous approach and use two pointers
        which points at the beginning and end of the array known as start,end

        Start inserting the Squared values of an array from backwards in an array
        by using two pointers to compare which absolute value is bigger.
    """
    # code for approach 1
    # sortedSquares = []
    # for value in array:
    #     sortedSquares.append(value**2)

    # sortedSquares.sort()

    # return sortedSquares

    # code for approach 2
    sortedSquares = [0 for _ in array]
    smallervalueidx = 0
    largervalueidx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallervalue = array[smallervalueidx]
        largervalue = array[largervalueidx]

        if abs(smallervalue) >= abs(largervalue):
            sortedSquares[idx] = smallervalue * smallervalue
            smallervalueidx += 1
        else:
            sortedSquares[idx] = largervalue * largervalue
            largervalueidx -= 1

    return sortedSquares


# array = [1,2,3,5,6,8,9]
arr = [-7, -5, -4, 3, 6, 8, 9]

result = sortedSquaredArray(arr)
print(result)
