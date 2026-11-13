from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity=capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        self[key]=value
        if len(self)>self.capacity:
            self.popitem(last=False)
        self.move_to_end(key)


def run_operations(operations, arguments):
    cache = None
    results = []

    for operation, args in zip(operations, arguments):
        if operation == "LRUCache":
            cache = LRUCache(*args)
            results.append(None)
        elif operation == "put":
            cache.put(*args)
            results.append(None)
        elif operation == "get":
            results.append(cache.get(*args))
        else:
            raise ValueError(f"Unknown operation: {operation}")

    return results


def run_tests():
    tests = [
        (
            "Given example",
            ["LRUCache", "put", "put", "get", "put", "get",
             "put", "get", "get", "get"],
            [[2], [1, 1], [2, 2], [1], [3, 3], [2],
             [4, 4], [1], [3], [4]],
            [None, None, None, 1, None, -1, None, -1, 3, 4],
        ),
        (
            "Get from empty cache",
            ["LRUCache", "get"],
            [[2], [10]],
            [None, -1],
        ),
        (
            "Capacity one",
            ["LRUCache", "put", "get", "put", "get", "get"],
            [[1], [1, 10], [1], [2, 20], [1], [2]],
            [None, None, 10, None, -1, 20],
        ),
        (
            "Update existing key without eviction",
            ["LRUCache", "put", "put", "put", "get", "get"],
            [[2], [1, 10], [2, 20], [1, 100], [1], [2]],
            [None, None, None, None, 100, 20],
        ),
        (
            "Get refreshes recency",
            ["LRUCache", "put", "put", "get", "put", "get", "get"],
            [[2], [1, 10], [2, 20], [1], [3, 30], [2], [1]],
            [None, None, None, 10, None, -1, 10],
        ),
        (
            "Update refreshes recency",
            ["LRUCache", "put", "put", "put", "put", "get", "get", "get"],
            [[2], [1, 10], [2, 20], [1, 100], [3, 30], [2], [1], [3]],
            [None, None, None, None, None, -1, 100, 30],
        ),
        (
            "Missing get does not change eviction order",
            ["LRUCache", "put", "put", "get", "put", "get", "get"],
            [[2], [1, 10], [2, 20], [99], [3, 30], [1], [2]],
            [None, None, None, -1, None, -1, 20],
        ),
        (
            "Zero key and zero value",
            ["LRUCache", "put", "put", "get", "get"],
            [[2], [0, 0], [1, 0], [0], [1]],
            [None, None, None, 0, 0],
        ),
        (
            "Reinsert an evicted key",
            ["LRUCache", "put", "put", "put", "get", "get"],
            [[1], [1, 10], [2, 20], [1, 100], [1], [2]],
            [None, None, None, None, 100, -1],
        ),
    ]

    passed = 0
    for name, operations, arguments, expected in tests:
        try:
            actual = run_operations(operations, arguments)
            assert actual == expected, (
                f"\n  Expected: {expected}\n  Actual:   {actual}"
            )
            print(f"PASS: {name}")
            passed += 1
        except Exception as error:
            print(f"FAIL: {name} — {error}")

    print(f"\n{passed}/{len(tests)} tests passed")


if __name__ == "__main__":
    run_tests()
