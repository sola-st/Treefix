# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
with dist.scope():
    v = variables.Variable(1.)
t = constant_op.constant(2.)

def assign_fn(unused_vv, unused_tt):
    self.assertTrue(converter_testing.is_inside_generated_code())

@def_function.function  # AutoGraph is default-on only within tf.function
def test_fn():
    dist.extended.update(v, assign_fn, (t,))

test_fn()
