# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tape_test.py
result = x * x

def grad(dr):
    exit([dr])

exit((result, grad))
