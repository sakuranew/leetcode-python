from typing import List
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_value(l:ListNode):
            r=[]
            while l.next:
                r.append(str(l.val))
                l=l.next
            r.append(str(l.val))
            r=int(''.join(r[::-1]))
            return r
        def to_list(v):
            head=ListNode(int(v[0]))
            cur=head
            for vv in v[1:]:
                cur.next=ListNode(int(vv))
                cur=cur.next
            return head
        l1=to_value(l1)
        l2=to_value(l2)

        return to_list(str(l1+l2)[::-1])

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head1 = l1
        head2 = l2
        while head1 or head2:
            sums = 0
            if not head2:
                sums = head1.val + carry
            else:
                sums = head1.val + head2.val + carry
            ones = sums % 10
            carry = sums // 10
            head1.val = ones

            if head2:
                head2 = head2.next
            if not head1.next and (head2 or carry):
                head1.next = ListNode(0)
            head1 = head1.next

        print(carry)

        return l1