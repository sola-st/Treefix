# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Add the function to the current context or a graph, if supplied.

    Args:
      g: the graph to add the function to. If not supplied, the function will
        be added to the current context.
      overwrite: A bool. If True, this function will overwrite any existing
        function of the same signature name in the graph `g` or context.
    """
# pylint: disable=protected-access
if not g and context.executing_eagerly():
    ctx = context.context()
    if ctx.has_function(self.name):
        if overwrite:
            ctx.remove_function(self.name)
            ctx.add_function_def(self.definition)
    else:
        ctx.add_function_def(self.definition)
else:
    if g._is_function(self.name):
        if overwrite:
            g._remove_function(self.name)
            g._add_function(self)
    else:
        g._add_function(self)

    for f in self.graph._functions.values():
        if g._is_function(f.name):
            if overwrite:
                g._remove_function(f.name)
                g._add_function(f)
        else:
            g._add_function(f)
