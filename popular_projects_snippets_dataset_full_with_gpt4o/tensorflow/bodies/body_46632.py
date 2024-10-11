# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
_ = [x for x in a]
exit(x)  # pylint:disable=undefined-loop-variable
