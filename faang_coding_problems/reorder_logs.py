class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        # TODO: Implement your solution here.
        digits_logs=[]
        letter_logs=[]
        for log in logs:
            if log[-1].isdigit():
                digits_logs.append(log)
            else:
                letter_logs.append(log)
        letter_logs.sort(key=lambda x:(x.split()[1:],x.split()[0]))
        result=letter_logs+digits_logs
        return result


def main() -> None:
    test_cases = [
        (
            "Example 1",
            ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
             "let2 own kit dig", "let3 art zero"],
            ["let1 art can", "let3 art zero", "let2 own kit dig",
             "dig1 8 1 5 1", "dig2 3 6"],
        ),
        (
            "Example 2",
            ["a1 9 2 3 1", "g1 act car", "zo4 4 7",
             "ab1 off key dog", "a8 act zoo"],
            ["g1 act car", "a8 act zoo", "ab1 off key dog",
             "a1 9 2 3 1", "zo4 4 7"],
        ),
        ("Single letter-log", ["a1 hello"], ["a1 hello"]),
        ("Single digit-log", ["d1 0"], ["d1 0"]),
        (
            "Only digit-logs preserve input order",
            ["z9 9 1", "a1 0 2", "m3 4 5"],
            ["z9 9 1", "a1 0 2", "m3 4 5"],
        ),
        (
            "Only letter-logs sort by content",
            ["a1 zebra", "z1 apple", "m1 banana"],
            ["z1 apple", "m1 banana", "a1 zebra"],
        ),
        (
            "Equal contents sort by identifier",
            ["let2 same words", "let10 same words", "let1 same words"],
            ["let1 same words", "let10 same words", "let2 same words"],
        ),
        (
            "Content takes priority over identifier",
            ["a1 zoo", "z9 apple"],
            ["z9 apple", "a1 zoo"],
        ),
        (
            "Content prefix sorts before longer content",
            ["a1 art zero", "z1 art", "b1 art can"],
            ["z1 art", "b1 art can", "a1 art zero"],
        ),
        (
            "Compare the full content",
            ["x1 art zoo", "x2 art apple", "x3 art banana"],
            ["x2 art apple", "x3 art banana", "x1 art zoo"],
        ),
        (
            "Interleaved types and equal letter contents",
            ["d9 8 3", "z1 act car", "d1 1 2", "a1 act car",
             "d5 8 3", "b1 act zoo"],
            ["a1 act car", "z1 act car", "b1 act zoo",
             "d9 8 3", "d1 1 2", "d5 8 3"],
        ),
        (
            "Identifiers do not determine log type",
            ["abc 12 34", "123 hello world", "xyz 0"],
            ["123 hello world", "abc 12 34", "xyz 0"],
        ),
        (
            "Already ordered",
            ["a1 apple", "b1 banana", "d2 9", "d1 1"],
            ["a1 apple", "b1 banana", "d2 9", "d1 1"],
        ),
    ]

    solution = Solution()
    passed = 0
    for name, logs, expected in test_cases:
        try:
            # Allow an in-place implementation without changing the test input.
            actual = solution.reorderLogFiles(logs.copy())
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
            print(f"  Input:    {logs}")
            print(f"  Expected: {expected}")
            print(f"  Actual:   {actual}")

    print(f"\n{passed}/{len(test_cases)} test cases passed.")
    if passed != len(test_cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
