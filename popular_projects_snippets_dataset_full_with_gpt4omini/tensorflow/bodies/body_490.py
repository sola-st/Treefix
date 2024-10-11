# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
# foo should be renamed to bar.
text = "import foo as f"
expected_text = "import bar as f"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "import foo"
expected_text = "import bar as foo"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "import foo.test"
expected_text = "import bar.test"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "import foo.test as t"
expected_text = "import bar.test as t"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)

text = "import foo as f, a as b"
expected_text = "import bar as f, a as b"
_, new_text = self._upgrade(RenameImports(), text)
self.assertEqual(expected_text, new_text)
