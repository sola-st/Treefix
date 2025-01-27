# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
t = constant_op.constant(2.)

def update_fn():
    self.assertTrue(converter_testing.is_inside_generated_code())

@def_function.function  # AutoGraph is default-on only within tf.function
def test_fn():
    dist.extended.update_non_slot(t, update_fn)

test_fn()
