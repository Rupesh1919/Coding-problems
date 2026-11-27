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


def zigzag_level_order_traversal(root: TreeNode) -> list[list[int]]:
    """Return odd levels left to right and even levels right to left."""
    rightToLeft=False
    q=deque([root])
    result=[]
    while q:
        count=len(q)
        current_list=[]
        for i in range(count):
            current=q.popleft()
            current_list.append(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        if rightToLeft:
            current_list=current_list[::-1]
        result.append(current_list)
        rightToLeft=not rightToLeft
    return result



def _build_tree(root_value: int, child_values: list[int | None]) -> TreeNode:
    """Build a tree from level-order child pairs, with None for missing children."""
    root = TreeNode(root_value)
    parents = deque([root])
    values = iter(child_values)
    while parents:
        parent = parents.popleft()
        left = next(values, None)
        right = next(values, None)
        if left is not None:
            parent.left = TreeNode(left)
            parents.append(parent.left)
        if right is not None:
            parent.right = TreeNode(right)
            parents.append(parent.right)
    return root


def _format_case(values: list[int | None] | list[list[int]]) -> str:
    if len(values) <= 20:
        return str(values)
    return f"[{str(values[:4])[1:-1]}, ..., {str(values[-4:])[1:-1]}]"


def run_tests() -> int:
    chain_values = []
    for value in range(1, 20_000):
        chain_values.extend([None, value])

    cases = [
        ("Example one", [1, 2, 3, 4], [[0], [2, 1], [3, 4]]),
        ("Example two", [None, 1, 2, None, None, 3], [[0], [1], [2], [3]]),
        ("Single node", [], [[0]]),
        (
            "Sparse tree with four levels",
            [2, 1, None, 5, 4, 3, 7, None, None, 6],
            [[0], [1, 2], [5, 4, 3], [6, 7]],
        ),
        ("20,000-node chain", chain_values, [[value] for value in range(20_000)]),
    ]

    passed = 0
    for name, child_values, expected in cases:
        print(name)
        print(f"  Input:    {_format_case([0, *child_values])}")
        print(f"  Expected: {_format_case(expected)}")
        try:
            actual = zigzag_level_order_traversal(_build_tree(0, child_values))
        except NotImplementedError:
            print("  PENDING (traversal is a stub)")
            continue

        print(f"  Actual:   {_format_case(actual)}")
        if actual == expected:
            passed += 1
            print("  PASS")
        else:
            print("  FAIL")

    print(f"\n{passed}/{len(cases)} tests passed.")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(run_tests())
