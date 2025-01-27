# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/break_statements_test.py
while x > 0:
    x -= 1
    if x % 2 == 0:
        break
