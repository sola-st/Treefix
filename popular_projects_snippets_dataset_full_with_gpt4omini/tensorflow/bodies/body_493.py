# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
text = "from bar import a as b"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(text, new_text)
