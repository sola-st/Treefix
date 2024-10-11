# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
ast_edits.NoUpdateSpec.__init__(self)
self.module_deprecations.update({"a.b": (ast_edits.ERROR, "a.b is evil.")})
