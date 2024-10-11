# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Test that we get the expected result if renaming kw2 to kw3."""
text = "f(a, b, kw1=c, kw2=d)\n"
expected = "f(a, b, kw1=c, kw3=d)\n"
(_, report, _), new_text = self._upgrade(RenameKeywordSpec(), text)
self.assertEqual(new_text, expected)
self.assertNotIn("Manual check required", report)

# No keywords specified, no reordering, so we should get input as output
text = "f(a, b, c, d)\n"
(_, report, _), new_text = self._upgrade(RenameKeywordSpec(), text)
self.assertEqual(new_text, text)
self.assertNotIn("Manual check required", report)

# Positional *args passed in that we cannot inspect, should warn
text = "f(a, *args)\n"
(_, report, _), _ = self._upgrade(RenameKeywordSpec(), text)
self.assertNotIn("Manual check required", report)

# **kwargs passed in that we cannot inspect, should warn
text = "f(a, b, kw1=c, **kwargs)\n"
(_, report, _), _ = self._upgrade(RenameKeywordSpec(), text)
self.assertIn("Manual check required", report)
