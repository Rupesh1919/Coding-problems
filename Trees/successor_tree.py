from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.parent: Optional[TreeNode] = None


def successor(node: TreeNode) -> Optional[TreeNode]:
    """Return the node's in-order successor."""
    if node.right:
        curr=node.right
        while curr.left is not None:
            curr=curr.left
        return curr
    curr=node
    while curr.parent is not None:
        if curr.parent.left is curr:
            return curr.parent
        curr=curr.parent
    return None


def _attach_left(parent: TreeNode, child: TreeNode) -> None:
    parent.left = child
    child.parent = parent


def _attach_right(parent: TreeNode, child: TreeNode) -> None:
    parent.right = child
    child.parent = parent


def run_tests() -> None:
    nodes = {value: TreeNode(value) for value in (20, 10, 30, 5, 15, 25, 35)}
    _attach_left(nodes[20], nodes[10])
    _attach_right(nodes[20], nodes[30])
    _attach_left(nodes[10], nodes[5])
    _attach_right(nodes[10], nodes[15])
    _attach_left(nodes[30], nodes[25])
    _attach_right(nodes[30], nodes[35])

    assert successor(nodes[5]) is nodes[10]
    assert successor(nodes[10]) is nodes[15]
    assert successor(nodes[15]) is nodes[20]
    assert successor(nodes[20]) is nodes[25]
    assert successor(nodes[30]) is nodes[35]
    assert successor(nodes[35]) is None

    print("All successor tests passed.")


if __name__ == "__main__":
    run_tests()