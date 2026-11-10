from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        # TODO: Implement your solution here.
        products.sort()
        n=len(products)
        l,j=0,n-1
        result=[]
        for i in range(len(searchWord)):
            while (l<=j) and (len(products[l])<=i or products[l][i]!=searchWord[i]):
                l+=1
            while (l<=j) and (len(products[j])<=i or products[j][i]!=searchWord[i]):
                j-=1
            total=j-l+1
            if total>=3:
                result.append([products[l],products[l+1],products[l+2]])
            elif total==2:
                result.append([products[l],products[l+1]])
            elif total==1:
                result.append([products[l]])
            else:
                result.append([])
        return result


def main() -> None:
    test_cases = [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            ["havana"],
            "havana",
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
        (
            ["mobile", "mouse"],
            "maz",
            [["mobile", "mouse"], [], []],
        ),
        # No products match even the first character.
        (["apple", "banana", "carrot"], "zoo", [[], [], []]),
        # Unsorted input; only the three smallest matches should be returned.
        (
            ["apricot", "application", "apple", "ape", "app"],
            "app",
            [["ape", "app", "apple"], ["ape", "app", "apple"],
             ["app", "apple", "application"]],
        ),
        # A product can be an exact match and a prefix of other products.
        (
            ["abc", "a", "abcd", "ab"],
            "abcde",
            [["a", "ab", "abc"], ["ab", "abc", "abcd"],
             ["abc", "abcd"], ["abcd"], []],
        ),
        # Exactly three matches, then two, then one.
        (
            ["dog", "deer", "deal"],
            "deer",
            [["deal", "deer", "dog"], ["deal", "deer"], ["deer"], ["deer"]],
        ),
        # The search word extends beyond the only product.
        (["cat"], "cats", [["cat"], ["cat"], ["cat"], []]),
        # A single character still requires sorting and truncation.
        (["azure", "atom", "apple", "ant"], "a", [["ant", "apple", "atom"]]),
        # Matching products lie between nonmatching products in sorted order.
        (
            ["zebra", "cat", "banana", "car", "apple", "carbon"],
            "car",
            [["car", "carbon", "cat"], ["car", "carbon", "cat"], ["car", "carbon"]],
        ),
        # Once a prefix fails, later characters cannot restore a match.
        (["abc", "abd", "bcd"], "axbc", [["abc", "abd"], [], [], []]),
    ]

    solution = Solution()
    passed = 0
    for index, (products, search_word, expected) in enumerate(test_cases, start=1):
        actual = solution.suggestedProducts(products.copy(), search_word)
        success = actual == expected
        passed += success
        print(f"Test case {index}: {'PASS' if success else 'FAIL'}")
        print(f"  Products: {products}")
        print(f"  Search word: {search_word!r}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}\n")

    print(f"{passed}/{len(test_cases)} test cases passed.")
    if passed != len(test_cases):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
