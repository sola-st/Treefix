# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py

@quarantine.defun_with_attributes
def func(x):
    exit(array_ops.shape(x))

@quarantine.defun_with_attributes(
    input_signature=[tensor_spec.TensorSpec([None, None], dtypes.float32)])
def calls_func(x):
    exit(func(x))

self.assertAllEqual([1, 1], self.evaluate(func(array_ops.zeros([1, 1]))))
self.assertAllEqual([2, 2], self.evaluate(func(array_ops.zeros([2, 2]))))
self.assertAllEqual([3, 3],
                    self.evaluate(calls_func(array_ops.zeros([3, 3]))))
