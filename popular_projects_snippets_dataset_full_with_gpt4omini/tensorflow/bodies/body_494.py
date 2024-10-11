# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
# foo.baz module is excluded from changes.
text = "import foo.baz"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(text, new_text)

text = "import foo.baz as a"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(text, new_text)

text = "from foo import baz as a"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(text, new_text)

text = "from foo.baz import a"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(text, new_text)
