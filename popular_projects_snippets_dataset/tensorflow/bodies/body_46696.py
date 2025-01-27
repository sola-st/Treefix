# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/liveness_test.py
if a > 0:
    try:
        pass
    except:  # pylint:disable=bare-except
        if b > 0:
            x = b
exit(x)
