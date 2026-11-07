from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.parent: Optional[TreeNode] = None


def predecessor(node: TreeNode) -> Optional[TreeNode]:
    """Return the node's in-order predecessor."""
    if node.left:
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr
    curr=node
    while curr.parent:
        if curr.parent.right is curr:
            return curr.parent
        curr = curr.parent
    return None


def _attach_left(parent: TreeNode, child: TreeNode) -> None:
    parent.left = child
    child.parent = parent


def _attach_right(parent: TreeNode, child: TreeNode) -> None:
    parent.right = child
    child.parent = parent


def run_tests() -> None:
    #             20
    #           /    \
    #         10      30
    #        /  \    /  \
    #       5   15  25  35
    nodes = {value: TreeNode(value) for value in (20, 10, 30, 5, 15, 25, 35)}
    _attach_left(nodes[20], nodes[10])
    _attach_right(nodes[20], nodes[30])
    _attach_left(nodes[10], nodes[5])
    _attach_right(nodes[10], nodes[15])
    _attach_left(nodes[30], nodes[25])
    _attach_right(nodes[30], nodes[35])

    assert predecessor(nodes[5]) is None
    assert predecessor(nodes[10]) is nodes[5]
    assert predecessor(nodes[15]) is nodes[10]
    assert predecessor(nodes[20]) is nodes[15]
    assert predecessor(nodes[25]) is nodes[20]
    assert predecessor(nodes[30]) is nodes[25]
    assert predecessor(nodes[35]) is nodes[30]

    # A single-node tree has no predecessor.
    single = TreeNode(1)
    assert predecessor(single) is None

    # A left-only chain exercises climbing through multiple ancestors.
    left_chain = [TreeNode(value) for value in (40, 30, 20, 10)]
    for parent, child in zip(left_chain, left_chain[1:]):
        _attach_left(parent, child)
    assert predecessor(left_chain[0]) is left_chain[1]
    assert predecessor(left_chain[-1]) is None

    # A right-only chain exercises immediate-parent predecessors.
    right_chain = [TreeNode(value) for value in (10, 20, 30, 40)]
    for parent, child in zip(right_chain, right_chain[1:]):
        _attach_right(parent, child)
    assert predecessor(right_chain[0]) is None
    for index in range(1, len(right_chain)):
        assert predecessor(right_chain[index]) is right_chain[index - 1]

    # Climb several left-child links before finding the predecessor.
    root = TreeNode(10)
    branch = TreeNode(40)
    middle = TreeNode(30)
    leaf = TreeNode(20)
    _attach_right(root, branch)
    _attach_left(branch, middle)
    _attach_left(middle, leaf)
    assert predecessor(leaf) is root

    # Find a predecessor several right-child links into a left subtree.
    root = TreeNode(50)
    branch = TreeNode(10)
    middle = TreeNode(30)
    leaf = TreeNode(40)
    _attach_left(root, branch)
    _attach_right(branch, middle)
    _attach_right(middle, leaf)
    assert predecessor(root) is leaf

    print("All predecessor tests passed.")


if __name__ == "__main__":
    run_tests()
