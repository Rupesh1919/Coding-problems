class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[] #pair (index,height)
        max_area=0
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                max_area=max(max_area,height*(i-index))
                start=index
            stack.append((start,h))
        while stack:
            index,height=stack.pop()
            max_area=max(max_area,height*(len(heights)-index))
        return max_area



def main() -> None:
    test_cases = [
        ("Example 1", [2, 1, 5, 6, 2, 3], 10),
        ("Example 2", [2, 4], 4),
        ("Single positive bar", [7], 7),
        ("Single zero bar", [0], 0),
        ("All zero bars", [0, 0, 0], 0),
        ("Equal heights", [3, 3, 3, 3], 12),
        ("Increasing heights", [1, 2, 3, 4, 5], 9),
        ("Decreasing heights", [5, 4, 3, 2, 1], 9),
        ("Zero splits the histogram", [3, 3, 0, 3, 3], 6),
        ("Lower bar connects both sides", [3, 2, 3, 3], 8),
        ("Tallest bar gives the largest area", [1, 8, 1], 8),
        ("Maximum length and height", [10_000] * 100_000, 1_000_000_000),
    ]

    solution = Solution()
    passed = 0
    for name, heights, expected in test_cases:
        try:
            actual = solution.largestRectangleArea(heights.copy())
        except NotImplementedError as error:
            print(error)
            raise SystemExit(1) from error
        except Exception as error:
            print(f"FAIL: {name} — {type(error).__name__}: {error}")
            continue

        success = actual == expected
        passed += success
        print(f"{'PASS' if success else 'FAIL'}: {name}")
        if not success:
            input_preview = (
                str(heights)
                if len(heights) <= 20
                else f"{heights[:20]} ... ({len(heights):,} bars)"
            )
            print(f"  Input:    {input_preview}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")

    print(f"\n{passed}/{len(test_cases)} test cases passed.")
    if passed != len(test_cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
