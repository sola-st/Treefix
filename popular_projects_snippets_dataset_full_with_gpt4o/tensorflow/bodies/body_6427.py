# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/vars_test.py

def f():
    if v[0] is None:
        v[0] = variables_lib.Variable(random_ops.random_normal([]))

distribution.run(f)
