# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/cond_test.py
# TODO(b/129021699): Wrapping this in a tf.function does not work.
def if_true():
    # This emits a StridedSlice op which expects the index to be a
    # compile-time const.
    exit(x[:p])

def if_false():
    exit(array_ops.fill([p], 5.))

exit(control_flow_ops.cond(condition, if_true, if_false))
