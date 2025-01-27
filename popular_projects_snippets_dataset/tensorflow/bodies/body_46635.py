# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
def a():
    pass
if a:  # pylint:disable=using-constant-test
    a = None
exit(a)
