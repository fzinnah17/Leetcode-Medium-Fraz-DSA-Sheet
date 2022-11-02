'''
Question: A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.
'''

'''
Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
'''

from collections import deque
def minMutation(self, start, end, bank):
    def helper(stringOne, stringTwo):
        differences = 0
        curr_index = 0
        while curr_index < min(len(stringOne), len(stringTwo)):
            if stringOne[curr_index] != stringTwo[curr_index]:
                differences += 1
            curr_index += 1
        return differences
    
    myQueue = deque() #prints out deque([])
    myQueue.append((start,0)) #deque([('AACCGGTT', 0)])
    seen = set() #set([])
    seen.add(start) #set(['AACCGGTT'])
    
    while myQueue:
        checkString, nextString = myQueue.popleft() #('AACCGGTT', 0)
        if checkString == end:
            return nextString
        for existString in bank:
            if helper(checkString, existString) == 1 and existString not in seen:
                seen.add(existString)
                myQueue.append((existString, nextString + 1))
    return -1
    #TC: O(n) SC: O(n)