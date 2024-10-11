# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/reaching_definitions_test.py
a = []
if b:
    try:
        pass
    except:  # pylint:disable=bare-except
        pass
exit(a)
