# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
"""Applies a function to each individual assignment.

    This function can process a possibly-unpacked (e.g. a, b = c, d) assignment.
    It tries to break down the unpacking if possible. In effect, it has the same
    effect as passing the assigned values in SSA form to apply_fn.

    Examples:

    The following will result in apply_fn(a, c), apply_fn(b, d):

        a, b = c, d

    The following will result in apply_fn(a, c[0]), apply_fn(b, c[1]):

        a, b = c

    The following will result in apply_fn(a, (b, c)):

        a = b, c

    It uses the visitor pattern to allow subclasses to process single
    assignments individually.

    Args:
      targets: list, tuple of or individual AST node. Should be used with the
        targets field of an ast.Assign node.
      values: an AST node.
      apply_fn: a function of a single argument, which will be called with the
        respective nodes of each single assignment. The signature is
        apply_fn(target, value), no return value.
    """
if not isinstance(targets, (list, tuple)):
    targets = (targets,)
for target in targets:
    if isinstance(target, (gast.Tuple, gast.List)):
        for i in range(len(target.elts)):
            target_el = target.elts[i]
            if isinstance(values, (gast.Tuple, gast.List)):
                value_el = values.elts[i]
            else:
                value_el = gast.Subscript(values, i, ctx=gast.Store())
            self.apply_to_single_assignments(target_el, value_el, apply_fn)
    else:
        # TODO(mdan): Look into allowing to rewrite the AST here.
        apply_fn(target, values)
