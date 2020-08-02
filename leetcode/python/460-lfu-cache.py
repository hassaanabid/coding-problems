"""
representation:
    node -> k, v, freq, next, prev
    freq_dic -> k:freq, v:(head,tail)
    head.next -> lru, tail.prev -> mru
    dic -> k: int, v: node
    self.min_freq : int, minimum frequency


example #1:
    LFUCache cache = new LFUCache( 2 /* capacity */ )
    cache.put(1, 1) ->
        dic = {1: node(1,1)}
        freq_dic = {1: [node(1,1)]}
        size = 1
        min_freq = 1
    cache.put(2, 2) ->
        dic = {1: node(1,1), 2: node(2,2) }
        freq_dic = {1: [node(1,1), node(2,2)]}
        size = 2
        min_freq = 1
    cache.get(1)    ->
        dic = {1: node(1,1), 2: node(2,2) }
        freq_dic = {1: [node(2,2), node(1,1)]}
        size = 2
        min_freq = 1
    cache.put(3, 3) ->
        dic = {1: node(1,1), 3: node(3,3) }
        freq_dic = {1: [node(1,1), node(3,3)]}
        size = 2
        min_freq = 1
    cache.get(2)    -> -1
    cache.get(3)    -> 3
    cache.put(4, 4) ->
        dic = {3: node(3,3),  4: node(4,4)}
        freq_dic = {1: [node(3,3), node(4,4)]}
        size = 2
        min_freq = 1
    cache.get(1)    -> -1
    cache.get(3)    -> 3
    cache.get(4)    -> 4

"""


class Node:
    def __init__(self, k, v, f):
        self.key = k
        self.value = v
        self.freq = f
        self.prev = None
        self.next = None


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.freq_dic = {}
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        # update freq
        node = self.dic[key]
        self.__update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # edge case
        if self.capacity == 0:
            return
        # replace value
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            # update freq
            self.__update_freq(node)
        # add a new k, v
        else:
            # evict first
            if len(self.dic) == self.capacity:
                head, tail = self.freq_dic[self.min_freq]
                lru = head.next
                self.__remove(lru)
                del self.dic[lru.key]

            node = Node(key, value, 1)
            self.dic[key] = node
            # case: init freq_dic
            if node.freq not in self.freq_dic:
                self.freq_dic[node.freq] = self.__list_init()
            head, tail = self.freq_dic[node.freq]
            self.__add(node, tail)
            # update freq to new k,v pair's f
            self.min_freq = 1
            # self.__print()

    def __list_init(self,):
        head = Node(-1, -1, -1)
        tail = Node(-1, -1, -1)
        head.next = tail
        tail.prev = head
        return (head, tail)

    def __is_empty(self, head):
        return head.next.next == None

    def __remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def __add(self, node, tail):
        last = tail.prev
        last.next = node
        tail.prev = node
        node.prev = last
        node.next = tail

    def __update_freq(self, node):
        freq = node.freq
        self.__remove(node)

        # case: node was last item in list
        if self.__is_empty(self.freq_dic[freq][0]):
            del self.freq_dic[freq]

        # case: min_freq == freq and no more items
        if self.min_freq == freq and freq not in self.freq_dic:
            self.min_freq += 1

        # case: init freq + 1
        if (freq + 1) not in self.freq_dic:
            self.freq_dic[freq + 1] = self.__list_init()

        # update frequency
        head, tail = self.freq_dic[freq + 1]
        node.freq += 1
        self.__add(node, tail)

    def __print_list(self, ptr):
        s = ''
        while ptr:
            s += f'[{ptr.key}, {ptr.value}], '
            ptr = ptr.next
        print(s)

    def __print(self,):
        print('dic', self.dic)
        print('freq_dic', self.freq_dic)
        for k, (h, t) in self.freq_dic.items():
            print('f: ', k)
            self.__print_list(h.next)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
