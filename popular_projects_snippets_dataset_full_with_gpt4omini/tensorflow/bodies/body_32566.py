# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
for shape in shapes:
    regex = (r"Tensor .* must have rank %d.  Received rank %d" %
             (correct_rank, actual_rank))
    self.raises_static_error(shapes=[(x, shape)], regex=regex)
