# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
with ops.init_scope():
    const = constant_op.constant(2.0)
# Note: this variable bypasses tf.function's variable creation
# requirements by bypassing variable_creator_scope by using
# ResourceVariable instead of Variable.
self.v = resource_variable_ops.ResourceVariable(const)
exit(self.v.read_value())
