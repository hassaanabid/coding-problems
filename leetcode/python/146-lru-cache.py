"""
Representation:
    Node has k, v, prev, next
    dic: dict #k: int, v: Node
    self.head.next # LRU
    self.tail.prev # most recently used
    invariant: len(dic) <= self.capacity
    
Example 1: 
    LRUCache cache = new LRUCache(2) -> capacity = 2, dic = {}, lis = [], size = 0
    cache.put(1, 1) -> dic = {1:Node(1,1)}, lis = [1], size = 1
    cache.put(2, 2) -> dic = {1:Node(1,1), 2:Node(2,2)}, lis = [1,2], size = 2
    cache.get(1)    -> dic[1].val -> 1 # dic = {1:Node(1,1), 2:Node(2,2)}, lis = [2,1], size = 2
    cache.put(3, 3) -> size == capacity -> dic = {1:Node(1), 3:Node(3,3)}, lis = [1,3], size = 2
    cache.get(2)    -> 2 not in dic -> True -> -1
    cache.put(4, 4) -> size == capacity -> dic = {4:Node(4,4), 3:Node(3,3)}, lis = [3,4], size = 2
    cache.get(1)    -> 1 in dic -> False -> -1
    cache.get(3)    -> 3 in dic -> True -> dic[3].val -> 3
    cache.get(4)    -> 4 in dic -> True -> dic[4].val -> 4

tricks:
    - use dummy nodes to avoid edge cases, remove
    - key is needed in node as well, in order to evict key from dic
"""
# credits: https://leetcode.com/problems/lru-cache/discuss/45926/Python-Dict-%2B-Double-LinkedList


class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}  # k: int, v: Node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            # adjust priority
            self.__remove(node)
            self.__add(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        # remove if exist
        if key in self.dic:
            node = self.dic[key]
            self.__remove(node)
        node = Node(key, value)
        self.__add(node)
        self.dic[key] = node  # add/replace
        # eviction
        if len(self.dic) > self.capacity:
            lru = self.head.next
            self.__remove(lru)
            del self.dic[lru.key]
        # self.__print_list()
        # print(self.dic)

    def __add(self, node: Node):
        """
            appends to tail
            add to middle logic due to dummy nodes
        """
        last = self.tail.prev
        last.next = node
        self.tail.prev = node
        node.prev = last
        node.next = self.tail

    def __remove(self, node):
        """
            remove middle logic due to dummy nodes
        """
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def __print_list(self,):
        s = ''
        ptr = self.head.next
        while ptr:
            s += f'[{ptr.key}, {ptr.value}], '
            ptr = ptr.next
        print(s)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
