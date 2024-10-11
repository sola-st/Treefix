# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf.py
"""Creates an ANF transformer.

    Args:
      ctx: transformer.Context
      config: Configuration
    """
super(AnfTransformer, self).__init__(ctx)
if config is None:
    # These could be pulled out, but are generally considered to already be in
    # A-normal form.  Thus they are left in by default, but could be pulled
    # out if the configuration calls for it.
    if gast_util.GAST2:
        literal_node_types = (
            gast.Num, gast.Str, gast.Bytes, gast.NameConstant,
            gast.Name  # Name is here to cover True, False, and None in Python 2
        )
    elif gast_util.GAST3:
        literal_node_types = (
            gast.Constant,
            gast.Name  # Name is here to cover True, False, and None in Python 2
        )
    else:
        assert False

    self._overrides = [
        (ASTEdgePattern(ANY, ANY, literal_node_types), LEAVE),
        (ASTEdgePattern(ANY, ANY, gast.expr), REPLACE)]
else:
    self._overrides = config
self._gensym = DummyGensym()
self._pending_statements = []
