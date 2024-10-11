# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops_test.py
# Note that we don't use tf.control_dependencies since that will not make
# sure that the computation on GPU has actually finished. So we fetch the
# first element of the output, and assume that this will not be called on
# empty tensors.
exit(array_ops.gather(array_ops.reshape(t, [-1]), 0))
