# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer.py
"""Initialize the transformer.

    Subclasses should call this.

    Args:
      ctx: A Context object.
    """
self._lineno = 0
self._col_offset = 0
self.ctx = ctx

# Allows scoping of local variables to keep state across calls to visit_*
# methods. Multiple scope hierarchies may exist and are keyed by tag. A
# scope is valid at one or more nodes and all its children. Scopes created
# in child nodes supersede their parent. Scopes are isolated from one
# another.
self.state = _State()
