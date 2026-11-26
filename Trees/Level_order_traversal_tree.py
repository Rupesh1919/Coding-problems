from __future__ import annotations
from collections import deque

from reprlib import repr as abbreviated_repr


class TreeNode:
    def __init__(self, value: int, children: list[TreeNode] | None = None) -> None:
        self.value = value
        self.children = [] if children is None else children


def level_order_traversal(root: TreeNode) -> list[list[int]]:
    """Return node values grouped by level, from left to right."""
    if root is None:
        return []
    q=deque([root])
    result=[]
    while q:
        count=len(q)
        current_list=[]
        for i in range(count):
            current=q.popleft()
            current_list.append(current.value)
            if current.children:
                for j in range(len(current.children)):
                    q.append(current.children[j])
        result.append(current_list)
    return result




def run_tests() -> int:
    # Choose child positions that produce the example outputs.
    example_one = TreeNode(1, [TreeNode(3, [TreeNode(5)]), TreeNode(4), TreeNode(2, [TreeNode(6)])])
    example_two = TreeNode(1, [TreeNode(2, [TreeNode(4, [TreeNode(3)])])])
    sparse = TreeNode(1, [TreeNode(2), TreeNode(4, [TreeNode(5), TreeNode(3)])])

    node_count = 20_000
    deep = TreeNode(1)
    current = deep
    for value in range(2, node_count + 1):
        child = TreeNode(value)
        current.children.append(child)
        current = child

    wide_values = list(range(node_count, 1, -1))
    wide = TreeNode(1, [TreeNode(value) for value in wide_values])
    cases = [
        ("Example one", example_one, [[1], [3, 4, 2], [5, 6]]),
        ("Example two", example_two, [[1], [2], [4], [3]]),
        ("Single node", TreeNode(1), [[1]]),
        ("Uneven branches", sparse, [[1], [2, 4], [5, 3]]),
        ("20,000-node chain", deep, [[value] for value in range(1, node_count + 1)]),
        ("20,000-node wide tree", wide, [[1], wide_values]),
    ]

    passed = 0
    for name, root, expected in cases:
        print(name)
        print(f"  Expected: {abbreviated_repr(expected)}")
        try:
            actual = level_order_traversal(root)
        except NotImplementedError:
            print("  PENDING (traversal is a stub)")
            continue

        matches = actual == expected
        passed += matches
        print(f"  Actual:   {abbreviated_repr(actual)}")
        print(f"  {'PASS' if matches else 'FAIL'}")

    print(f"\n{passed}/{len(cases)} tests passed.")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(run_tests())
