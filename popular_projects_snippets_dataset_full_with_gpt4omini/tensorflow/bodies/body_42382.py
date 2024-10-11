# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with context.device('gpu:0'):
    v = resource_variable_ops.ResourceVariable(1.0)
with context.device('cpu:0'):
    # Check that even though we specified the cpu device we'll run the read op
    # in the device where the handle is.
    self.assertAllEqual(
        gen_resource_variable_ops.read_variable_op(v.handle, v.dtype), 1.0)
