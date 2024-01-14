  class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}

    def get(self, key: int) -> int:
        if key in self.lru.keys():
            x = self.lru[key]
            del self.lru[key]
            self.lru[key] = x
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru.keys():
            del self.lru[key]
            self.lru[key] = value
        else:  
            if len(self.lru.keys()) == self.capacity:
                del self.lru[list(self.lru.keys())[0]]
                self.lru[key] = value
            else:
                self.lru[key] = value





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
