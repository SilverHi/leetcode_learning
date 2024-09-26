from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#思考思路：
#从题目里很轻易的就能想到基础解法，即拿到链表遍历节点，然后得到该链表对应的数字，接着将两个数字相加，最后在拆分成链表的结构并返回
#但这里很明显有更优的思路，由于链表中每个节点存储的是每个数位上的值，我们可以直接对两个链表上同位的数字进行求和，直接得到最终的链表，省去的中间将链表解析为数字的过程
#但这个思路需要解决加法中进位的实现，即如何保证本位中满十进一可以正确的向下一位传递。我想这应该也是这道题核心考察的地方

#这个过程让我想起了如何自己实现计算器这个练习demo中涉及到的抽象语法树（AST），不过与此题无关不深究了

#输入的两个链表不等长，在递归中需要注意递归的边界判断

class Solution:

    def getNewLinkedList(self,l1: Optional[ListNode], l2: Optional[ListNode],plusflag:int)->Optional[ListNode]:
        l1val = 0
        l2val = 0
        l1nextflag = False
        l2nextflag = False
        l1next = None
        l2next = None
        if l1 is not None:
            l1val = l1.val
            l1nextflag = l1.next is not None
            if l1nextflag:
                l1next = l1.next
        if l2 is not None:
            l2val = l2.val
            l2nextflag = l2.next is not None
            if l2nextflag:
                l2next = l2.next
        newval = l1val + l2val +plusflag
        if newval >= 10:
            plusflag = 1
            newval = newval - 10
        else:
            plusflag = 0
        node = ListNode()
        node.val = newval
        if l1nextflag or l2nextflag or plusflag==1:
            nextNode=self.getNewLinkedList(l1next,l2next,plusflag)
            node.next = nextNode
            return node
        else:
            return node
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.getNewLinkedList(l1,l2,0)



