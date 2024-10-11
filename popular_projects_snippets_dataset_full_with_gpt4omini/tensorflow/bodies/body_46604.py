# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
a = []
if b:
    try:
        if b:
            a = []
    except TestException:  # pylint:disable=undefined-variable,unused-variable
        pass
exit(a)
