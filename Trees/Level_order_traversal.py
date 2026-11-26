from __future__ import annotations
from collections import deque

class TreeNode:
    def __init__(
        self,
        value: int,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def level_order_traversal(root: TreeNode) -> list[list[int]]:
    """Return node values grouped by depth, from left to right."""
    if root is None:
        return []
    q=deque([root])
    result=[]
    while q:
        count=len(q)
        current=[]
        for i in range(count):
            cur_ele=q.popleft()
            current.append(cur_ele.value)
            if cur_ele.left:
                q.append(cur_ele.left)
            if cur_ele.right:
                q.append(cur_ele.right)
        result.append(current)
    return result



def _format_levels(levels: list[list[int]]) -> str:
    if len(levels) <= 8:
        return str(levels)
    return f"[{str(levels[:4])[1:-1]}, ..., {str(levels[-4:])[1:-1]}] ({len(levels):,} levels)"


def run_tests() -> None:
    # The first example specifies the levels, so either child side works.
    chain = TreeNode(0, TreeNode(1, right=TreeNode(2, TreeNode(4, TreeNode(3)))))
    balanced = TreeNode(
        2,
        TreeNode(5, TreeNode(0), TreeNode(1)),
        TreeNode(4, TreeNode(3), TreeNode(6)),
    )
    sparse = TreeNode(
        0,
        TreeNode(1, right=TreeNode(4)),
        TreeNode(2, left=TreeNode(3)),
    )

    node_count = 20_000
    deep = TreeNode(0)
    current = deep
    for value in range(1, node_count):
        current.right = TreeNode(value)
        current = current.right

    cases = [
        ("example one", chain, [[0], [1], [2], [4], [3]]),
        ("example two", balanced, [[2], [5, 4], [0, 1, 3, 6]]),
        ("single node", TreeNode(0), [[0]]),
        ("sparse tree", sparse, [[0], [1, 2], [4, 3]]),
        ("maximum-depth tree", deep, [[value] for value in range(node_count)]),
    ]
    passed = 0
    for name, root, expected in cases:
        actual = level_order_traversal(root)
        matches = actual == expected
        passed += matches
        print(f"{name}: {'PASS' if matches else 'FAIL'}")
        print(f"  Expected: {_format_levels(expected)}")
        print(f"  Actual:   {_format_levels(actual)}")

    print(f"\n{passed}/{len(cases)} level-order traversal tests passed.")
    if passed != len(cases):
        raise SystemExit(1)


if __name__ == "__main__":
    run_tests()
