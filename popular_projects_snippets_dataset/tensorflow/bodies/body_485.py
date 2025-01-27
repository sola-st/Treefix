# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Same as testRemoveDeprecatedKeywordAndReorder but on g2 (more args)."""
text = "g2(a, b, kw1=x, c=c, d=d)\n"
acceptable_outputs = [
    "g2(a, b, c=c, d=d, kw1=x)\n",
    "g2(a=a, b=b, kw1=x, c=c, d=d)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasAndReorderRest(), text)
self.assertIn(new_text, acceptable_outputs)

# Keywords are reordered, so we should reorder arguments too
text = "g2(a, b, x, c, d)\n"
# Don't accept an output which doesn't reorder c and d
acceptable_outputs = [
    "g2(a, b, c, d, x)\n",
    "g2(a=a, b=b, kw1=x, c=c, d=d)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasAndReorderRest(), text)
self.assertIn(new_text, acceptable_outputs)

# If we used the alias, it should get renamed
text = "g2(a, b, kw1_alias=x, c=c, d=d)\n"
acceptable_outputs = [
    "g2(a, b, kw1=x, c=c, d=d)\n",
    "g2(a, b, c=c, d=d, kw1=x)\n",
    "g2(a=a, b=b, kw1=x, c=c, d=d)\n",
    "g2(a=a, b=b, c=c, d=d, kw1=x)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasKeyword(), text)
self.assertIn(new_text, acceptable_outputs)

# It should get renamed and reordered even if it's not in order
text = "g2(a, b, d=d, c=c, kw1_alias=x)\n"
acceptable_outputs = [
    "g2(a, b, kw1=x, c=c, d=d)\n",
    "g2(a, b, c=c, d=d, kw1=x)\n",
    "g2(a, b, d=d, c=c, kw1=x)\n",
    "g2(a=a, b=b, kw1=x, c=c, d=d)\n",
    "g2(a=a, b=b, c=c, d=d, kw1=x)\n",
    "g2(a=a, b=b, d=d, c=c, kw1=x)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasKeyword(), text)
self.assertIn(new_text, acceptable_outputs)
