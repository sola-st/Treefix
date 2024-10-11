# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
text = "f(a, b, kw1=c, kw2=d)\n"
_, new_text = self._upgrade(ast_edits.NoUpdateSpec(), text)
self.assertEqual(new_text, text)

text = "f(a, b, c, d)\n"
_, new_text = self._upgrade(ast_edits.NoUpdateSpec(), text)
self.assertEqual(new_text, text)
