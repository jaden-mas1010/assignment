# Data Structures & Systems Design Assignment

Solutions for the Avaloka (Guruvai Sciences) AI / Multi-Agent Systems Intern assessment.

## Problems

- **LRU Cache:** `LRUCache(capacity)` with `get(key)` and `put(key, value)`; dictionary + doubly linked list.
- **Event Scheduler:** `can_attend_all(events)` and `min_rooms_required(events)`; sorting + min-heap.

Both solutions use Python's standard library only.

## Run

```bash
python assignment.py
python test_assignment.py
```

## Example

```python
from assignment import LRUCache, can_attend_all, min_rooms_required

cache = LRUCache(2)
cache.put(1, "Apple")
cache.put(2, "Banana")
cache.get(1)
cache.put(3, "Cherry")
print(cache.get(2))  # -1

meetings = [(9, 11), (10, 12), (11, 13)]
print(can_attend_all(meetings))       # False
print(min_rooms_required(meetings))  # 2
```

Adjacent meetings, such as (9, 10) and (10, 11), are allowed. The scheduler assumes valid intervals (start < end).

## Complexity

| Function | Average/worst-case time | Extra space |
| --- | --- | --- |
| `LRUCache.get` / `put` | O(1) average | O(1) per call; O(C) cache total |
| `can_attend_all` | O(n log n) | O(n) |
| `min_rooms_required` | O(n log n) | O(n) |

C is cache capacity; n is the number of meetings.

**Author:** Jaden Mascarenhas
