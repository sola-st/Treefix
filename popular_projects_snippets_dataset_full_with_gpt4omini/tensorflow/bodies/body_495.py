# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
text = "import foo.bar as a, foo.baz as b, foo.baz.c, foo.d"
expected_text = "import bar.bar as a, foo.baz as b, foo.baz.c, bar.d"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "from foo import baz, a, c"
expected_text = """from foo import baz
from bar import a, c"""
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)
