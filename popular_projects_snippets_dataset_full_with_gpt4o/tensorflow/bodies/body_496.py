# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
text = """
def t():
  from c import d
  from foo import baz, a
  from e import y
"""
expected_text = """
def t():
  from c import d
  from foo import baz
  from bar import a
  from e import y
"""
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)
