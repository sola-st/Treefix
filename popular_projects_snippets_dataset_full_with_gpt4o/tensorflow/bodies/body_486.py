# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Remove multiple keywords at once."""
# Not using deprecated keywords -> no rename
text = "h(a, kw1=x, kw2=y)\n"
_, new_text = self._upgrade(RemoveMultipleKeywordArguments(), text)
self.assertEqual(new_text, text)

# Using positional arguments (in proper order) -> no change
text = "h(a, x, y)\n"
_, new_text = self._upgrade(RemoveMultipleKeywordArguments(), text)
self.assertEqual(new_text, text)

# Use only the old names, in order
text = "h(a, kw1_alias=x, kw2_alias=y)\n"
acceptable_outputs = [
    "h(a, x, y)\n",
    "h(a, kw1=x, kw2=y)\n",
    "h(a=a, kw1=x, kw2=y)\n",
    "h(a, kw2=y, kw1=x)\n",
    "h(a=a, kw2=y, kw1=x)\n",
]
_, new_text = self._upgrade(RemoveMultipleKeywordArguments(), text)
self.assertIn(new_text, acceptable_outputs)

# Use only the old names, in reverse order, should give one of same outputs
text = "h(a, kw2_alias=y, kw1_alias=x)\n"
_, new_text = self._upgrade(RemoveMultipleKeywordArguments(), text)
self.assertIn(new_text, acceptable_outputs)

# Mix old and new names
text = "h(a, kw1=x, kw2_alias=y)\n"
_, new_text = self._upgrade(RemoveMultipleKeywordArguments(), text)
self.assertIn(new_text, acceptable_outputs)
