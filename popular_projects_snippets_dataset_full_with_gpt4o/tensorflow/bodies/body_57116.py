# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/broadcast_gradient_args.py
"""Build the op testing graph."""
input1 = tf.compat.v1.placeholder(dtype=parameters['dtype'], name='input1')
input2 = tf.compat.v1.placeholder(dtype=parameters['dtype'], name='input2')
output1, output2 = tf.raw_ops.BroadcastGradientArgs(s0=input1, s1=input2)
exit(([input1, input2], [output1, output2]))
