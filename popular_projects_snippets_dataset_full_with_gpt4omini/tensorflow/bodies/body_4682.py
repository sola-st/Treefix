# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
with dist.scope():
    v = variables.Variable(1.)
t = constant_op.constant(2.)

def assign_fn(vv, tt):
    self.assertIs(vv, v)
    self.assertIs(tt, t)
dist.extended.update(v, assign_fn, (t,))
