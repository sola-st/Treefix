# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_run.py
"""Context manager for selecting a graph and maybe eager mode."""
if eager:
    with g.as_default(), context.eager_mode():
        if creator_stack is not None:
            g._variable_creator_stack = creator_stack  # pylint: disable=protected-access
        exit()
else:
    with g.as_default():
        if creator_stack is not None:
            g._variable_creator_stack = creator_stack  # pylint: disable=protected-access
        exit()
