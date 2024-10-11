# Extracted from ./data/repos/black/src/black/linegen.py
if node.children[0].type == token.AWAIT and len(node.children) > 1:
    if (
        node.children[1].type == syms.atom
        and node.children[1].children[0].type == token.LPAR
    ):
        if maybe_make_parens_invisible_in_atom(
            node.children[1],
            parent=node,
            remove_brackets_around_comma=True,
        ):
            wrap_in_parentheses(node, node.children[1], visible=False)

        # Since await is an expression we shouldn't remove
        # brackets in cases where this would change
        # the AST due to operator precedence.
        # Therefore we only aim to remove brackets around
        # power nodes that aren't also await expressions themselves.
        # https://peps.python.org/pep-0492/#updated-operator-precedence-table
        # N.B. We've still removed any redundant nested brackets though :)
        opening_bracket = cast(Leaf, node.children[1].children[0])
        closing_bracket = cast(Leaf, node.children[1].children[-1])
        bracket_contents = cast(Node, node.children[1].children[1])
        if bracket_contents.type != syms.power:
            ensure_visible(opening_bracket)
            ensure_visible(closing_bracket)
        elif (
            bracket_contents.type == syms.power
            and bracket_contents.children[0].type == token.AWAIT
        ):
            ensure_visible(opening_bracket)
            ensure_visible(closing_bracket)
            # If we are in a nested await then recurse down.
            remove_await_parens(bracket_contents)
