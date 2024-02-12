"""
Problem Statement:
    An array consist of distinct integer values and value K.
    
    array = [3,5,-4,8,11,1-1,6]
    k = 10

    Find a function whether a pair exists that sum up to K.

"""


def twoNumberSum(array, targetNum):
    """
        Approach 1:
        Time Complexity: O(N^2),Space Complexity: O(1)
        using Nested for loop.

    ______________________________________________________________________________

        Approach 2:
        Time Complexity: O(Nlog(N)),Space Complexity: O(1)

        We will sort the elements in an array using Quicksort,MergeSort,etc.
        Then we will use 2-pointer method where pointers are
        left_pointer:  which points to the array[0] --> smallest number
        right_pointer: which points to the array[n-1] -> Largest number

        we will increment left_pointer when required sum is less
        i.e., array[left] + array[right] < k and we will decrement right_pointer
        when required sum is greater than k.i.e., array[left] + array[right] > k

        if we found i.e., array[left] + array[right] == k
                    return [array[left] + array[right]]


    ____________________________________________________________________________________

        Approach 3:
        Time Complexity: O(N),Space Complexity: O(N)

        We will implement a hashtable which will be dicitionary in python data type.
        we will iterate through each value of an array and substract with K and
        check the desired value(k-i) is present in hashtable if not iterate through
        an array for next element and append "i:True" in hashtbale and search for the
        entire values of array you will find a pair that exists in array.

        if exists:
            return [i,j]
        else:
            return []

    """
    # Code for Approach 1

    # for i in range(len(array) - 1):
    #     firstNum = array[i]
    #     for j in range(i+1,len(array)):
    #         secondNum = array[j]
    #         if firstNum + secondNum == targetNum:
    #             return [firstNum,secondNum]

    # return []

    # code for Approach 2:

    # array.sort() # built-in python function
    # left = 0
    # right = len(array) - 1
    # while left<right:
    #     currentSum = array[left] + array[right]
    #     if currentSum == targetNum:
    #         return [array[left],array[right]]
    #     elif currentSum < targetNum:
    #         left += 1
    #     elif currentSum > targetNum:
    #         right -= 1
    # return []

    # Code for Approach 3:
    nums = {}
    for num in array:
        potentialMatch = targetNum - num
        if potentialMatch in nums:
            return [num, potentialMatch]
        else:
            nums[num] = True
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetNum = 10

pair = twoNumberSum(array, targetNum)

print(pair)
