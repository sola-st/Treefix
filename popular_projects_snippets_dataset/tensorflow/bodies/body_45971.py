# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
a = 1
if a > 2:
    _ = 'b'
    if a < 5:
        _ = 'c'
    _ = 'd'
