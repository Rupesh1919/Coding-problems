from __future__ import annotations

from typing import Optional


class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.parent: Optional[TreeNode] = None


def delete_node(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    """Delete value from a BST with unique values and return the updated root.

    Keep parent pointers correct. If value is absent, leave the tree unchanged.
    Either copying a replacement value or transplanting a node is allowed.
    """

    if root is None:
        return None
    curr=root
    while curr and curr.value != value:
        if curr.value>value:
            curr=curr.left
        else:
            curr=curr.right
    if not curr:
        return root
    if not curr.left and not curr.right:
        return leaf_node(curr,root)
    elif curr.left and curr.right:
        return two_children_node(curr,root)
    else:
        return one_child_node(curr,root)

def one_child_node(current:TreeNode,root: TreeNode)->TreeNode:
    # if current.parent is None:
    #     root=
    # if current.parent.left is current:
    #     if current.left:
    #             current.parent.left=current.left
    #     else:
    #             current.parent.left=current.right
    # else:
    #     if current.left:
    #         current.parent.right=current.left
    #     else:
    #         current.parent.right=current.right
    child=None
    if current.left:
        child=current.left
    else:
        child=current.right
    if current.parent is None:
        root=child
        child.parent=None
        return root
    if current.parent.left is current:
        current.parent.left=child
        child.parent=current.parent
    else:
        current.parent.right=child
        child.parent=current.parent
    return root



def two_children_node(current:TreeNode,root:TreeNode)->TreeNode:
    min=current.right
    prev=current
    while min.left:
        prev=min
        min=min.left
    current.value=min.value
    if min is prev.left:
        prev.left=min.right
    else:
        prev.right=min.right
    if min.right:
        min.right.parent=prev       
    return root


def leaf_node(current:TreeNode,root:TreeNode)->TreeNode:
    if root.value==current.value:
        return None
    if current.parent.left is current:
        current.parent.left=None
        current.parent=None
    else:
        current.parent.right=None
        current.parent=None
    return root



def _attach_left(parent: TreeNode, child: TreeNode) -> None:
    parent.left = child
    child.parent = parent


def _attach_right(parent: TreeNode, child: TreeNode) -> None:
    parent.right = child
    child.parent = parent


def _build_tree() -> TreeNode:
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
    return nodes[20]


def _assert_tree(root: Optional[TreeNode], expected: list[int]) -> None:
    """Check contents, BST ordering, parent pointers, and absence of cycles."""
    values: list[int] = []
    seen: set[int] = set()

    def visit(node: Optional[TreeNode], parent: Optional[TreeNode]) -> None:
        if node is None:
            return
        assert id(node) not in seen, "Cycle or shared child detected"
        seen.add(id(node))
        assert node.parent is parent, f"Incorrect parent for {node.value}"
        visit(node.left, node)
        values.append(node.value)
        visit(node.right, node)

    visit(root, None)
    assert values == expected, f"Expected {expected}, got {values}"
    assert all(a < b for a, b in zip(values, values[1:])), "Invalid BST ordering"


def run_tests() -> None:
    assert delete_node(None, 10) is None

    # Delete the only node; an absent value should preserve a single node.
    root = delete_node(TreeNode(10), 10)
    _assert_tree(root, [])
    root = delete_node(TreeNode(10), 99)
    _assert_tree(root, [10])

    # Fresh trees isolate leaf, internal-node, root, and absent-value cases.
    for value in (5, 35, 10, 30, 20, 99):
        root = delete_node(_build_tree(), value)
        expected = [v for v in (5, 10, 15, 20, 25, 30, 35) if v != value]
        _assert_tree(root, expected)

    # Delete a root with only a left child or only a right child.
    for attach in (_attach_left, _attach_right):
        root = TreeNode(20)
        child = TreeNode(10 if attach is _attach_left else 30)
        attach(root, child)
        root = delete_node(root, 20)
        _assert_tree(root, [child.value])

    # Delete a non-root node with one child, on either side of its parent.
    for branch_value, attach_branch in ((20, _attach_left), (80, _attach_right)):
        for offset, attach_child in ((-10, _attach_left), (10, _attach_right)):
            root = TreeNode(50)
            branch = TreeNode(branch_value)
            child = TreeNode(branch_value + offset)
            attach_branch(root, branch)
            attach_child(branch, child)
            root = delete_node(root, branch_value)
            _assert_tree(root, sorted([50, child.value]))

    # Two-child deletion with a deeper replacement that has its own child.
    # Both successor-based and predecessor-based implementations are supported.
    root = _build_tree()
    assert root.left is not None and root.left.right is not None
    assert root.right is not None and root.right.left is not None
    _attach_left(root.left.right, TreeNode(12))
    _attach_right(root.right.left, TreeNode(27))
    root = delete_node(root, 20)
    _assert_tree(root, [5, 10, 12, 15, 25, 27, 30, 35])

    # Repeated deletions must keep returning a usable root, down to an empty tree.
    root = _build_tree()
    remaining = [5, 10, 15, 20, 25, 30, 35]
    for value in (20, 5, 30, 10, 35, 15, 25):
        root = delete_node(root, value)
        remaining.remove(value)
        _assert_tree(root, remaining)
    assert delete_node(root, 99) is None

    print("All BST deletion tests passed.")


if __name__ == "__main__":
    run_tests()
