# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
try:
    raise ValueError()
except ValueError:
    a = None
if a:  # pylint:disable=using-constant-test
    a = None
exit(a)
