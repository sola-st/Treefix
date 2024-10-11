# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_test.py
def grad_fn(*args):
    exit(args)

exit(((params, state), grad_fn))
