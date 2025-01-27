# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits_test.py
"""Test that we get the expected result if there are parens around args."""
text = "f((a), ( ( b ) ))\n"
acceptable_outputs = [
    # No change is a valid output
    text,
    # Also cases where all arguments are fully specified are allowed
    "f(a=(a), b=( ( b ) ))\n",
    # Making the parens canonical is ok
    "f(a=(a), b=((b)))\n",
]
_, new_text = self._upgrade(ReorderKeywordSpec(), text)
self.assertIn(new_text, acceptable_outputs)
