# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/cond.py
"""Build the graph for cond tests."""
input1 = tf.compat.v1.placeholder(dtype=parameters["dtype"], shape=(1,))
input2 = tf.compat.v1.placeholder(dtype=parameters["dtype"], shape=(1,))
# MLIR TFLite converter can't handle scalar inputs. This is a workaround
# to input (1,) tensors and then reshape to scalar.
# TODO(b/129003347): Remove the workaround after scalar inputs are
# supported.
pred = tf.compat.v1.placeholder(dtype=tf.bool, shape=(1,))
pred_scalar = tf.reshape(pred, ())

out = tf.cond(
    pred=pred_scalar, true_fn=lambda: input1, false_fn=lambda: input2)
exit(([input1, input2, pred], [out]))
