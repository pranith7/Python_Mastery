def isValidSubsequence(array, sequence):

    seqidx = 0
    for value in array:
        if value == sequence[seqidx]:
            seqidx += 1
        if seqidx == len(sequence):
            breaK
    return seqidx == len(sequence)


def ValidSubsequence(array, sequence):
    """
    Implementing Two Pointer Approach for two check if Sequence is a
    validSubsequence for array.

    As you can see we are using two variables arridx,seqidx to point out the
    indices for their respective arrays and we are iterating over the array using
    while loop.

    if we found a match we increase seqidx by 1 and we increase arridx irrespecitve
    of the above condition and after the iteration of the whole array
    we return True or False by using this condition: return seqidx == len(sequence)

    """
    arridx = 0
    seqidx = 0
    while arridx < len(array) and seqidx < len(sequence):
        if array[arridx] == sequence[seqidx]:
            seqidx += 1
        arridx += 1
    return seqidx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10, 4]

result = ValidSubsequence(array, sequence)
print(result)
