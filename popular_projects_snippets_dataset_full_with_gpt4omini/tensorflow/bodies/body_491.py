# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
# foo should be renamed to bar.
text = "from foo import a"
expected_text = "from bar import a"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "from foo.a import b"
expected_text = "from bar.a import b"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "from foo import *"
expected_text = "from bar import *"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "from foo import a, b"
expected_text = "from bar import a, b"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)
