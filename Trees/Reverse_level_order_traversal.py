from __future__ import annotations

from reprlib import repr as abbreviated_repr
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


def reverse_level_order_traversal(root: TreeNode) -> list[list[int]]:
    """Return levels from deepest to shallowest, each from left to right."""
    q=deque([root])
    result=[]
    while q:
        current_list=[]
        count=len(q)
        for i in range(count):
            current=q.popleft()
            current_list.append(current.value)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        result.append(current_list)
    return result[::-1]


def _tree_values(root: TreeNode) -> list[int | None]:
    values: list[int | None] = []
    pending: deque[TreeNode | None] = deque([root])
    while pending:
        node = pending.popleft()
        if node is None:
            values.append(None)
        else:
            values.append(node.value)
            pending.extend((node.left, node.right))

    while values and values[-1] is None:
        values.pop()
    return values


def _format_case(values: list) -> str:
    if len(values) <= 20:
        return str(values)
    return f"[{str(values[:3])[1:-1]}, ..., {str(values[-3:])[1:-1]}]"


def run_tests() -> int:
    example_one = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2))
    example_two = TreeNode(0, right=TreeNode(1, TreeNode(2, right=TreeNode(3))))
    sparse = TreeNode(
        0,
        TreeNode(2, right=TreeNode(5)),
        TreeNode(1, TreeNode(4, TreeNode(6)), TreeNode(3)),
    )

    node_count = 20_000
    deep = TreeNode(0)
    current = deep
    for value in range(1, node_count):
        current.right = TreeNode(value)
        current = current.right

    cases = [
        ("Example one", example_one, [[3, 4], [1, 2], [0]]),
        ("Example two", example_two, [[3], [2], [1], [0]]),
        ("Single node", TreeNode(0), [[0]]),
        ("Sparse tree with unsorted levels", sparse, [[6], [5, 4, 3], [2, 1], [0]]),
        ("20,000-node chain", deep, [[value] for value in range(node_count - 1, -1, -1)]),
    ]

    passed = 0
    for name, root, expected in cases:
        print(name)
        print(f"  Input:    {_format_case(_tree_values(root))}")
        print(f"  Expected: {_format_case(expected)}")
        try:
            actual = reverse_level_order_traversal(root)
        except NotImplementedError:
            print("  PENDING (traversal is a stub)")
            continue
        except Exception as error:
            print(f"  ERROR ({type(error).__name__}: {error})")
            continue

        if actual == expected:
            passed += 1
            print("  PASS")
        else:
            print("  FAIL")
            print(f"  Actual:   {abbreviated_repr(actual)}")

    print(f"\n{passed}/{len(cases)} tests passed.")
    return 0 if passed == len(cases) else 1


if __name__ == "__main__":
    raise SystemExit(run_tests())
