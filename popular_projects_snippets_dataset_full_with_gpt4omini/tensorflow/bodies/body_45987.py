# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
x = 1
if x > 0:
    x = 1
    x += 3
exit(x)
