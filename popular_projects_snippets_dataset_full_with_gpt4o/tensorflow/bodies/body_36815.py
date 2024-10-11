# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/control_flow_ops_py_test.py
if tf2.enabled():
    # In TF1 do not wrap with tf.function so that we can test the v1 control
    # flow code path.
    exit(eager_def_function.function(f))
exit(f)
