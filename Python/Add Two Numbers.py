# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addWithCarry(self, l1, l2, carry):
        if l1 == None and l2 == None:
            if (carry != 0):
                cur = ListNode(0)
                cur.val = carry 
                return cur 
            return None
        if l1 == None:
            return Solution.addWithCarry(self, l2, l1, carry)
        result = ListNode(0)
        cur = result
        pre = None
        # print 1, id(pre)
        while l1 != None:
            # print 0
            # print 2, id(pre)
            cur.val = (l1.val + carry) % 10
            carry = (l1.val + carry) / 10
            pre = cur
            cur = ListNode(carry)
            pre.next = cur
            l1 = l1.next
            # print pre.next.val
            # print 3, id(pre)
        # print pre.next.val
        # print 4, id(pre)
        if pre.next.val == 0:
            pre.next = None

        return result

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        cur = res
        pre = None
        carry = 0

        while l1 != None and l2 != None:
            # print l2.next, l1.next
            cur.val = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) / 10
            pre = cur
            cur = ListNode(0)
            pre.next = cur
            l1 = l1.next
            l2 = l2.next

        cur = Solution.addWithCarry(self, l1, l2, carry)
        pre.next = cur
        return res




        
if __name__ == '__main__':
    sl = Solution()

    l1a = ListNode(2)
    l1b = ListNode(4)
    l1c = ListNode(3)
    l1a.next = l1b
    l1b.next = l1c

    l2a = ListNode(5)
    l2b = ListNode(6)
    l2c = ListNode(4)
    l2d = ListNode(0)
    l2a.next = l2b
    l2b.next = l2c
    l2c.next = l2d

    res = sl.addTwoNumbers(l1a, l2a)

    while res != None:
        print res.val,
        res = res.next