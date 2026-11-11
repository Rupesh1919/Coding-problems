from collections import Counter
from typing import List
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # TODO: Implement your solution here.
        distances=[]
        result=[]
        for x,y in points:
            current_distance=math.sqrt(x**2+y**2)
            distances.append((current_distance,x,y))
        distances.sort(key=lambda x:-(x[0]))
        while k>0:
            d,x,y=distances.pop()
            result.append([x,y])
            k-=1
        return result
        


def main() -> None:
    # Expected results may be returned in any order. Each case has a unique
    # selection at the kth distance (ties within the selection are allowed).
    test_cases = [
        ("Example 1", [[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ("Example 2", [[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ("Single point", [[7, -8]], 1, [[7, -8]]),
        ("All points", [[3, 4], [0, 0], [-1, 2]], 3,
         [[3, 4], [0, 0], [-1, 2]]),
        ("Origin is closest", [[9, 9], [0, 0], [-1, -1]], 1, [[0, 0]]),
        ("Negative coordinates", [[-5, -5], [-1, -2], [-3, -4]], 2,
         [[-1, -2], [-3, -4]]),
        ("Points on axes", [[0, 5], [-2, 0], [0, -1], [4, 0]], 2,
         [[0, -1], [-2, 0]]),
        ("Equal distances within selection", [[1, 0], [0, -1], [3, 3]], 2,
         [[1, 0], [0, -1]]),
        ("Duplicate points", [[1, 1], [4, 4], [1, 1], [2, 2]], 2,
         [[1, 1], [1, 1]]),
        ("Coordinate limits", [[10000, 10000], [-10000, 0], [9999, 0]], 2,
         [[9999, 0], [-10000, 0]]),
        ("Squared distance versus coordinate sum", [[3, 3], [5, 0], [0, 6]], 1,
         [[3, 3]]),
        ("Closest point appears last", [[10, 10], [8, 8], [6, 6], [1, 1]], 1,
         [[1, 1]]),
        ("Maximum number of points", [[x, 0] for x in range(10000)], 3,
         [[0, 0], [1, 0], [2, 0]]),
    ]

    solution = Solution()
    passed = 0
    for name, points, k, expected in test_cases:
        try:
            # Copy each point so an in-place solution cannot change test input.
            actual = solution.kClosest([point[:] for point in points], k)
            # Counter checks both order independence and duplicate counts.
            success = (
                len(actual) == k
                and Counter(map(tuple, actual)) == Counter(map(tuple, expected))
            )
        except NotImplementedError as error:
            print(error)
            raise SystemExit(1) from error
        except Exception as error:
            print(f"FAIL: {name} — {type(error).__name__}: {error}")
            continue

        passed += success
        print(f"{'PASS' if success else 'FAIL'}: {name}")
        if not success:
            print(f"  k: {k}")
            print(f"  Expected (any order): {expected}")
            print(f"  Actual: {actual}")

    print(f"\n{passed}/{len(test_cases)} test cases passed.")
    if passed != len(test_cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
