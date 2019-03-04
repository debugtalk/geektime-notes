#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (52.74%)
# Total Accepted:    518.2K
# Total Submissions: 982.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
#
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution1:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head:
#             return None

#         stack = []
#         while head:
#             stack.append(head.val)
#             head = head.next

#         node = ListNode(stack.pop())
#         reversed_head = node
#         while True:
#             try:
#                 item = stack.pop()
#                 node.next = ListNode(item)
#                 node = node.next
#             except IndexError:
#                 break

#         return reversed_head


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        return prev

# testcases
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def prepare_linkedlist(self, nums):
        if len(nums) == 0:
            return None

        node = ListNode(nums[0])
        head = node
        for num in nums[1:]:
            node.next = ListNode(num)
            node = node.next

        return head

    def read_linked_list(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        return nums

    def test_1(self):
        nums = [1,2,3,4,5]
        raw_link_head = self.prepare_linkedlist(nums)
        reversed_head = self.s.reverseList(raw_link_head)
        self.assertEqual(
            self.read_linked_list(reversed_head),
            [5,4,3,2,1]
        )


    def test_2(self):
        nums = []
        raw_link_head = self.prepare_linkedlist(nums)
        reversed_head = self.s.reverseList(raw_link_head)
        self.assertEqual(
            self.read_linked_list(reversed_head),
            []
        )


if __name__ == "__main__":
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    testcase = loader.loadTestsFromTestCase(TestSolution)
    runner.run(testcase)
