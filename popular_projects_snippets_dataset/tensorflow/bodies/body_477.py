# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
text = "a.b.c(a.b.x)"
(_, _, errors), new_text = self._upgrade(ModuleDeprecationSpec(), text)
self.assertEqual(text, new_text)
self.assertIn("Using member a.b.c", errors[0])
self.assertIn("1:0", errors[0])
self.assertIn("Using member a.b.c", errors[0])
self.assertIn("1:6", errors[1])
