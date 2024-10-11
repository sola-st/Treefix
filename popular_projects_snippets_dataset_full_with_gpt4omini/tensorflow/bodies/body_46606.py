# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
a = []
if b:
    try:
        pass
    except TestException as e:  # pylint:disable=undefined-variable,unused-variable
        if b:
            a = []
exit(a)
