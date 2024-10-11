# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Test that we get the expected result if kw2 is now before kw1."""
text = "f(a, b, kw1=c, kw2=d)\n"
acceptable_outputs = [
    # No change is a valid output
    text,
    # Just reordering the kw.. args is also ok
    "f(a, b, kw2=d, kw1=c)\n",
    # Also cases where all arguments are fully specified are allowed
    "f(a=a, b=b, kw1=c, kw2=d)\n",
    "f(a=a, b=b, kw2=d, kw1=c)\n",
]
(_, report, _), new_text = self._upgrade(ReorderKeywordSpec(), text)
self.assertIn(new_text, acceptable_outputs)
self.assertNotIn("Manual check required", report)

# Keywords are reordered, so we should reorder arguments too
text = "f(a, b, c, d)\n"
acceptable_outputs = [
    "f(a, b, d, c)\n",
    "f(a=a, b=b, kw1=c, kw2=d)\n",
    "f(a=a, b=b, kw2=d, kw1=c)\n",
]
(_, report, _), new_text = self._upgrade(ReorderKeywordSpec(), text)
self.assertIn(new_text, acceptable_outputs)
self.assertNotIn("Manual check required", report)

# Positional *args passed in that we cannot inspect, should warn
text = "f(a, b, *args)\n"
(_, report, _), _ = self._upgrade(ReorderKeywordSpec(), text)
self.assertIn("Manual check required", report)

# **kwargs passed in that we cannot inspect, should warn
text = "f(a, b, kw1=c, **kwargs)\n"
(_, report, _), _ = self._upgrade(ReorderKeywordSpec(), text)
self.assertNotIn("Manual check required", report)
