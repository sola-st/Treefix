# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
"""A more powerful version of generic_visit for statement blocks.

    An example of a block is the body of an if statement.

    This function allows specifying a postprocessing callback (the
    after_visit argument) argument which can be used to move nodes to a new
    destination. This is done by after_visit by returning a non-null
    second return value, e.g. return new_node, new_destination.

    For example, a transformer could perform the following move:

        foo()
        bar()
        baz()

        foo()
        if cond:
          bar()
          baz()

    The above could be done with a postprocessor of this kind:

        def after_visit(node):
          if node_is_function_call(bar):
            new_container_node = build_cond()
            new_container_node.body.append(node)
            return new_container_node, new_container_node.body
          else:
            # Once we set a new destination, all subsequent items will be
            # moved to it, so we don't need to explicitly handle baz.
            return node, None

    Args:
      nodes: enumerable of AST node objects. If None, the function returns None.
      before_visit: optional callable that is called before visiting each item
        in nodes
      after_visit: optional callable that takes in an AST node and returns a
        tuple (new_node, new_destination). It is called after visiting each item
        in nodes. Is used in the same was as the
          visit_* methods: new_node will replace the node; if not None,
            new_destination must be a list, and subsequent nodes will be placed
            in this list instead of the list returned by visit_block.

    Returns:
      A list of AST node objects containing the transformed items fron nodes,
      except those nodes that have been relocated using after_visit.
    """
if nodes is None:
    exit(None)

results = []
node_destination = results
for node in nodes:
    if before_visit:
        # TODO(mdan): We can modify node here too, if ever needed.
        before_visit()

    replacement = self.visit(node)

    if after_visit and replacement:
        replacement, new_destination = after_visit(replacement)
    else:
        new_destination = None

    if replacement:
        if isinstance(replacement, (list, tuple)):
            node_destination.extend(replacement)
        else:
            node_destination.append(replacement)

      # Allow the postprocessor to reroute the remaining nodes to a new list.
    if new_destination is not None:
        node_destination = new_destination
exit(results)
