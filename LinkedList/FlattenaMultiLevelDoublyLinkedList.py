'''
Question: You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.
Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.
Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.


Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]'''


def flatten(self, head):
    #The idea is to iterate through the linked list and keep on iterating for the next pointer, but also to check if there is any child node of any of the nodes. If there is any child node, then we have to check if there is any next value of that node. If so, then the next linked list values will go to the stack. Then, the head.next pointer will become the children values. Also, the children value's previous value will be the head. After we are completely done iterating through the linked list, we will take out the value from the stack one at a time from the end and later on return the head.
    
    stack = [] #stack to keep the next values in
    start = head #temporary variable to hold the head
    
    while head: #as long as the head value exists
        if head.child: #check if there is any child value
            if head.next: #if so, then check if there was any next value
                stack.append(head.next) #then put the next value inside the stack
            head.next = head.child #then the new next value is the child
            head.next.prev = head #new child's previous value is the head
            head.child = None #and there are no more child value
        if head.next == None and len(stack) != 0: #after we reach the end of the linked list and as we see our stack is not empty
            head.next = stack.pop() #take out the nodes from the end of the stack and the last linked list node's next value should be that popped value
            head.next.prev = head #that value's previous value is the head
        head = head.next #we have to follow the above process for all the next values of head inside the linked list
    return start #we have to return the temporary variable
    #TC: O(n) SC: O(n)