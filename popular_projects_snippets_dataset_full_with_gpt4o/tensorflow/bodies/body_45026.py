# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/impl/api_test.py
if needs_autograph:
    if constant_op.constant(True):
        x = constant_op.constant(1)
    else:
        x = constant_op.constant(2)
else:
    x = 3
exit(x)
