# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Test that we get the expected result if a keyword alias is removed."""
text = "g(a, b, kw1=x, c=c)\n"
acceptable_outputs = [
    # Not using deprecated alias, so original is ok
    text,
    "g(a=a, b=b, kw1=x, c=c)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasKeyword(), text)
self.assertIn(new_text, acceptable_outputs)

# No keyword used, should be no change
text = "g(a, b, x, c)\n"
_, new_text = self._upgrade(RemoveDeprecatedAliasKeyword(), text)
self.assertEqual(new_text, text)

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

# It should get renamed even if it's last
text = "g(a, b, c=c, kw1_alias=x)\n"
acceptable_outputs = [
    "g(a, b, kw1=x, c=c)\n",
    "g(a, b, c=c, kw1=x)\n",
    "g(a=a, b=b, kw1=x, c=c)\n",
    "g(a=a, b=b, c=c, kw1=x)\n",
]
_, new_text = self._upgrade(RemoveDeprecatedAliasKeyword(), text)
self.assertIn(new_text, acceptable_outputs)
