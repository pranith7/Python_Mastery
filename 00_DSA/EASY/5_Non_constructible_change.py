""" 
Problem Statement:
    Given a list of positive integers representing the denominations of available coins,
    return the smallest positive integer that cannot be obtained through any combination
    of these coins. If all possible combinations can result in every positive integer, then
    the function should return None or null depending upon language syntax support.

    Example:
    Input: coins=[1, 2, 5]
    Output: 4
    Explanation: Although we can obtain 1, 2, 3, and 5, we can't reach 4 because the next
    higher value after 5 is already greater than what we want to achieve.


"""


def nonConstructibleChange(coins):
    """
    Approaches used in this implementation include sorting and iterative traversal of sorted array.
        Time complexity: O(N*log(N)), where N is the length of the coins list.
                         This accounts for the time required to sort the list.
        Space complexity: O(1), assuming the additional space required during sorting is
                          negligible compared to the size of the inputs.
    """
    # Code for Approach 1
    currentChangeCreated = 0
    coins.sort()
    if coins[0] != 1:
        return 1
    for coin in coins:
        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        currentChangeCreated += coin
    # pass
    return currentChangeCreated + 1


coins = [5, 7, 1, 1, 2, 3, 22]
change = nonConstructibleChange(coins)
print(change)
