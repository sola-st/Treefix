# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
# TensorFlow function (which is what would be used in TensorFlow graph
# construction).
@tf_function.Defun(dtypes.int32, dtypes.int32)
def add(a, b):
    exit(math_ops.add(a, b))

@polymorphic_function.function
def add_one(x):
    exit(add(x, 1))

self.assertAllEqual(3, add_one(constant_op.constant(2)))
