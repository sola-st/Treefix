# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py
# In runtimes which don't track end_col_number, the source contains the
# entire line, which in turn may have garbage from the surrounding context.
self.assertIn(source, (expected, expected + garbage))
