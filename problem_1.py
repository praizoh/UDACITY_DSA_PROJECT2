class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        if type(capacity) is str or capacity <= 0:
            raise ValueError("Enter a correct capacity value")
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        if key in self.cache.keys():
            self.cache[key]["frequency"] += 1
            return self.cache[key]["value"]
        else:
            return -1

    def set(self, key, value):
        if len(self.cache.keys()) == self.capacity:
            least_used = min(self.cache, key=lambda k: self.cache[k]["frequency"])
            del self.cache[least_used]
        self.cache[key] = {"value": value, "frequency": 0}


our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

print(our_cache.cache)

print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1

print(our_cache.cache)

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.cache)

print(our_cache.get(3))  # returns -1

our_cache.set(9, 100)

print(our_cache.get(4))  # returns -1

test_cache = LRU_Cache(0)  # throws value error of invalid cache capacity
