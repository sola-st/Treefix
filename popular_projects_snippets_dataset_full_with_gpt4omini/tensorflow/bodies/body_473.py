# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
RemoveDeprecatedAliasKeyword.__init__(self)
# Note that these should be in the old order.
self.function_reorders["g"] = ["a", "b", "kw1", "c"]
self.function_reorders["g2"] = ["a", "b", "kw1", "c", "d"]
