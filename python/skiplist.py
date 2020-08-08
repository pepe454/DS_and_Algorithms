from random import random


class LLNode:
    def __init__(self, val, next_node=None, down_node=None):
        self.val = val
        self.next = next_node
        self.down = down_node

    def __str__(self):
        list_str = f"{self.val}"
        curr_node = self.next
        while curr_node is not None:
            list_str += f"->{curr_node.val}"
            curr_node = curr_node.next
        return list_str


class Skiplist:
    def __init__(self):
        self.height = 6
        self.sentinel = LLNode(float("-inf"))
        curr_node = self.sentinel
        for i in range(self.height-1):  # create 5 list heads below sentinel
            curr_node.down = LLNode(float("-inf"))
            curr_node = curr_node.down

    def search(self, target: int) -> bool:
        curr_node = self.sentinel
        for level in range(self.height):
            while curr_node.next is not None and curr_node.next.val < target:
                curr_node = curr_node.next
            if curr_node.next is None or curr_node.next.val > target:  # search down
                curr_node = curr_node.down
            else:  # curr_node.next.val must == target
                return True
        return False

    def add(self, num: int) -> None:
        nodes = []  # each next value in these will be num
        curr_node = self.sentinel
        for level in range(self.height):  # maybe this should be height - 1?
            while curr_node.next is not None and curr_node.next.val < num:
                curr_node = curr_node.next
            nodes.append(curr_node)
            curr_node = curr_node.down

        # now we're at the bottom of the skiplist
        last_node = None
        for node in nodes[::-1]:
            new_node = LLNode(num, node.next, last_node)
            node.next = new_node
            last_node = new_node
            if random() < 0.5:
                break

    def erase(self, num: int) -> bool:
        curr_node = self.sentinel
        found = False
        for level in range(self.height):
            while curr_node.next is not None and curr_node.next.val < num:
                curr_node = curr_node.next
            if curr_node.next is not None and curr_node.next.val == num:  # keep going down but delete next
                del_node = curr_node.next
                curr_node.next = curr_node.next.next
                del_node = None
                found = True
            curr_node = curr_node.down

        return False

    def dump(self):
        curr_node = self.sentinel
        while curr_node is not None:
            print(f"[{curr_node}]")
            curr_node = curr_node.down
