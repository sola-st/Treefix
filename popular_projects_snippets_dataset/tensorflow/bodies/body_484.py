# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Test for when a keyword alias is removed and args are reordered."""
text = "g(a, b, kw1=x, c=c)\n"
acceptable_outputs = [
    "g(a, b, c=c, kw1=x)\n",
    "g(a=a, b=b, kw1=x, c=c)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasAndReorderRest(), text)
self.assertIn(new_text, acceptable_outputs)

# Keywords are reordered, so we should reorder arguments too
text = "g(a, b, x, c)\n"
# Don't accept an output which doesn't reorder c and d
acceptable_outputs = [
    "g(a, b, c, x)\n",
    "g(a=a, b=b, kw1=x, c=c)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasAndReorderRest(), text)
self.assertIn(new_text, acceptable_outputs)

# If we used the alias, it should get renamed
text = "g(a, b, kw1_alias=x, c=c)\n"
acceptable_outputs = [
    "g(a, b, kw1=x, c=c)\n",
    "g(a, b, c=c, kw1=x)\n",
    "g(a=a, b=b, kw1=x, c=c)\n",
    "g(a=a, b=b, c=c, kw1=x)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasKeyword(), text)
self.assertIn(new_text, acceptable_outputs)

# It should get renamed and reordered even if it's last
text = "g(a, b, c=c, kw1_alias=x)\n"
acceptable_outputs = [
    "g(a, b, kw1=x, c=c)\n",
    "g(a, b, c=c, kw1=x)\n",
    "g(a=a, b=b, kw1=x, c=c)\n",
    "g(a=a, b=b, c=c, kw1=x)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasKeyword(), text)
self.assertIn(new_text, acceptable_outputs)
