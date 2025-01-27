# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
a = 1
while a:
    _ = 'a'
    if a > 2:
        _ = 'b'
        while True:
            raise '1'
    if a > 3:
        _ = 'c'
        while True:
            raise '1'
