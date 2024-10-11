# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/from_sparse_tensor_slices_test.py
slices = [[1., 2., 3.], [1.], [1.], [1., 2.], [], [1., 2.], [], [], []]

verify_fn(
    self,
    lambda: self._build_sparse_tensor_slice_dataset(slices),
    num_outputs=9,
    sparse_tensors=True)
