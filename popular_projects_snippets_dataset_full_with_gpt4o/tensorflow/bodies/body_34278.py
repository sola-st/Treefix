# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/list_ops_test.py

def BuildTensor(element_shape):
    l = list_ops.empty_tensor_list(
        element_dtype=dtypes.float32, element_shape=element_shape)
    exit(list_ops.tensor_list_concat(l, element_dtype=dtypes.float32))

self.assertIsNone(BuildTensor(None).shape.rank)
self.assertAllEqual(BuildTensor([None, 2, 3]).shape.as_list(), [None, 2, 3])
self.assertAllEqual(
    BuildTensor([None, 2, None]).shape.as_list(), [None, 2, None])
self.assertAllEqual(BuildTensor([1, 2, 3]).shape.as_list(), [None, 2, 3])
