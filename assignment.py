class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")

        self.capacity = capacity
        self.cache = {}

 
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous

    def _add_recent(self, node):
        
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def _move_to_recent(self, node):
        self._remove(node)
        self._add_recent(node)

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_recent(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_recent(node)
            return

        if len(self.cache) == self.capacity:
            oldest = self.head.next
            self._remove(oldest)
            del self.cache[oldest.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._add_recent(new_node)


import heapq


def can_attend_all(events):
    sorted_events = sorted(events)

    for i in range(1, len(sorted_events)):
        previous_end = sorted_events[i - 1][1]
        current_start = sorted_events[i][0]

        if current_start < previous_end:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    sorted_events = sorted(events)
    rooms = []  # Min-heap of end times
    max_rooms = 0

    for start, end in sorted_events:
        
        while rooms and rooms[0] <= start:
            heapq.heappop(rooms)

        heapq.heappush(rooms, end)
        max_rooms = max(max_rooms, len(rooms))

    return max_rooms


def run_examples():
    cache = LRUCache(2)
    cache.put(1, "Apple")
    cache.put(2, "Banana")
    assert cache.get(1) == "Apple"
    cache.put(3, "Cherry")
    assert cache.get(2) == -1
    cache.put(1, "Updated")
    assert cache.get(1) == "Updated"

    assert can_attend_all([(9, 10), (10, 11), (11, 12)])
    assert not can_attend_all([(9, 12), (10, 11)])
    assert min_rooms_required([(9, 11), (10, 12), (11, 13)]) == 2
    assert min_rooms_required([(9, 11), (10, 12),(11, 13), (10, 11)]) == 3
    assert can_attend_all([])
    assert min_rooms_required([]) == 0


if __name__ == "__main__":
    run_examples()
    print("All example tests passed.")
