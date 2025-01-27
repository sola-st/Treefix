# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Test that we get the expected result if kw2 is renamed and moved."""
text = "f(a, b, kw1=c, kw2=d)\n"
acceptable_outputs = [
    "f(a, b, kw3=d, kw1=c)\n",
    "f(a=a, b=b, kw1=c, kw3=d)\n",
    "f(a=a, b=b, kw3=d, kw1=c)\n",
]
(_, report, _), new_text = self._upgrade(
    ReorderAndRenameKeywordSpec(), text)
self.assertIn(new_text, acceptable_outputs)
self.assertNotIn("Manual check required", report)

# Keywords are reordered, so we should reorder arguments too
text = "f(a, b, c, d)\n"
acceptable_outputs = [
    "f(a, b, d, c)\n",
    "f(a=a, b=b, kw1=c, kw3=d)\n",
    "f(a=a, b=b, kw3=d, kw1=c)\n",
]
(_, report, _), new_text = self._upgrade(
    ReorderAndRenameKeywordSpec(), text)
self.assertIn(new_text, acceptable_outputs)
self.assertNotIn("Manual check required", report)

# Positional *args passed in that we cannot inspect, should warn
text = "f(a, *args, kw1=c)\n"
(_, report, _), _ = self._upgrade(ReorderAndRenameKeywordSpec(), text)
self.assertIn("Manual check required", report)

# **kwargs passed in that we cannot inspect, should warn
text = "f(a, b, kw1=c, **kwargs)\n"
(_, report, _), _ = self._upgrade(ReorderAndRenameKeywordSpec(), text)
self.assertIn("Manual check required", report)
