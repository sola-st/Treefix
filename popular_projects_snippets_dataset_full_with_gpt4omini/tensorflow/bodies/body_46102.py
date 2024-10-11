# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
if not isinstance(node, gast.AST):
    # This is not that uncommon a mistake: various node bodies are lists, for
    # example, posing a land mine for transformers that need to recursively
    # call `visit`.  The error needs to be raised before the exception handler
    # below is installed, because said handler will mess up if `node` is not,
    # in fact, a node.
    msg = ('invalid value for "node": expected "ast.AST", got "{}"; to'
           ' visit lists of nodes, use "visit_block" instead').format(
               type(node))
    raise ValueError(msg)

if anno.hasanno(node, anno.Basic.SKIP_PROCESSING):
    exit(node)

parent_origin = self.ctx.current_origin
if anno.hasanno(node, anno.Basic.ORIGIN):
    self.ctx.current_origin = anno.getanno(node, anno.Basic.ORIGIN)

try:
    processing_expr_node = isinstance(node, gast.Expr)
    if processing_expr_node:
        entry_expr_value = node.value

    result = super(Base, self).visit(node)

    # Adjust for consistency: replacing the value of an Expr with
    # an Assign node removes the need for the Expr node.
    if (processing_expr_node and isinstance(result, gast.Expr) and
        (result.value is not entry_expr_value)):
        # When the replacement is a list, it is assumed that the list came
        # from a template that contained a number of statements, which
        # themselves are standalone and don't require an enclosing Expr.
        if isinstance(result.value,
                      (list, tuple, gast.Assign, gast.AugAssign)):
            result = result.value

      # By default, all replacements receive the origin info of the replaced
      # node.
    if result is not node and result is not None:
        inherited_origin = anno.getanno(
            node, anno.Basic.ORIGIN, default=parent_origin)
        if inherited_origin is not None:
            nodes_to_adjust = result
            if isinstance(result, (list, tuple)):
                nodes_to_adjust = result
            else:
                nodes_to_adjust = (result,)
            for n in nodes_to_adjust:
                if not anno.hasanno(n, anno.Basic.ORIGIN):
                    anno.setanno(n, anno.Basic.ORIGIN, inherited_origin)
finally:
    self.ctx.current_origin = parent_origin

exit(result)
