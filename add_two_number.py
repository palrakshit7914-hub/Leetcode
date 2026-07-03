class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next




class Solution:
    def add_two_numbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.value if l1 else 0
            val2 = l2.value if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
    
# ---- for your own value(example) -----

def build_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def print_list(node):
    values = []
    while node:
        values.append(str(node.value))
        node = node.next
    print("[" + ", ".join(values) + "]")


if __name__ == "__main__":
    l1 = build_list([2, 2, 2])
    l2 = build_list([3, 3, 3])
    result = Solution().add_two_numbers(l1, l2)
    print_list(result)  # Output: [5, 5, 5]