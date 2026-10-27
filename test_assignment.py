import unittest
from assignment import LRUCache, can_attend_all, min_rooms_required


class TestLRUCache(unittest.TestCase):
    def test_lru_eviction(self):
        cache = LRUCache(2)
        cache.put(1, "Apple")
        cache.put(2, "Banana")
        self.assertEqual(cache.get(1), "Apple")
        cache.put(3, "Cherry")
        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), "Apple")

    def test_update_and_capacity_one(self):
        cache = LRUCache(1)
        cache.put(1, "A")
        cache.put(1, "B")
        self.assertEqual(cache.get(1), "B")
        cache.put(2, "C")
        self.assertEqual(cache.get(1), -1)

    def test_invalid_capacity(self):
        with self.assertRaises(ValueError):
            LRUCache(0)


class TestEventScheduler(unittest.TestCase):
    def test_adjacent_events(self):
        events = [(9, 10), (10, 11), (11, 12)]
        self.assertTrue(can_attend_all(events))
        self.assertEqual(min_rooms_required(events), 1)

    def test_overlapping_events(self):
        events = [(9, 11), (10, 12), (11, 13)]
        self.assertFalse(can_attend_all(events))
        self.assertEqual(min_rooms_required(events), 2)

    def test_three_rooms(self):
        events = [(9, 11), (10, 12), (11, 13), (10, 11)]
        self.assertEqual(min_rooms_required(events), 3)

    def test_empty_events(self):
        self.assertTrue(can_attend_all([]))
        self.assertEqual(min_rooms_required([]), 0)

    def test_input_not_modified(self):
        events = [(11, 12), (9, 10), (10, 11)]
        before = events.copy()
        can_attend_all(events)
        min_rooms_required(events)
        self.assertEqual(events, before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
