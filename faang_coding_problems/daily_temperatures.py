class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack=[] # pair (index, temperature)
        result=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and stack[-1][1]<t:
                index,prev_t=stack.pop()
                result[index]=i-index
            stack.append([i,t])
        return result
                


def main() -> None:
    test_cases = [
        ("Example 1", [73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ("Example 2", [30, 40, 50, 60], [1, 1, 1, 0]),
        ("Example 3", [30, 60, 90], [1, 1, 0]),
        ("Single day", [30], [0]),
        ("Decreasing temperatures", [100, 90, 70, 30], [0, 0, 0, 0]),
        ("Equal temperatures", [70, 70, 70], [0, 0, 0]),
        ("Equal days before a warmer day", [70, 70, 71], [2, 1, 0]),
        ("First warmer day wins", [70, 60, 71, 100], [2, 1, 1, 0]),
        (
            "Maximum length with a warmer final day",
            [30] * 99_999 + [100],
            list(range(99_999, -1, -1)),
        ),
    ]

    solution = Solution()
    passed = 0
    for name, temperatures, expected in test_cases:
        try:
            actual = solution.dailyTemperatures(temperatures.copy())
        except NotImplementedError as error:
            raise SystemExit(str(error)) from error
        except Exception as error:
            print(f"FAIL: {name} ({type(error).__name__}: {error})")
            continue

        if actual == expected:
            print(f"PASS: {name}")
            passed += 1
        else:
            print(f"FAIL: {name}")
            if len(temperatures) <= 20:
                print(f"  Input:    {temperatures}")
                print(f"  Expected: {expected}")
                print(f"  Actual:   {actual}")
            else:
                print(f"  Expected {len(expected):,} answers, starting with {expected[:5]}")
                if isinstance(actual, list):
                    print(f"  Got {len(actual):,} answers, starting with {actual[:5]}")
                else:
                    print(f"  Got {type(actual).__name__}")

    print(f"\n{passed}/{len(test_cases)} test cases passed.")
    if passed != len(test_cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
