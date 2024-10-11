# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/edit_distance_op_test.py
# Shape inference figures out the shape from the shape variables
# Explicit tuple() needed since zip returns an iterator in Python 3.
expected_shape = [
    max(h, t) for h, t in tuple(zip(hypothesis[2], truth[2]))[:-1]
]

# SparseTensorValue inputs.
with ops.Graph().as_default() as g, self.session(g):
    # hypothesis and truth are (index, value, shape) tuples
    self._testEditDistanceST(
        hypothesis_st=sparse_tensor.SparseTensorValue(
            *[ConstantOf(x) for x in hypothesis]),
        truth_st=sparse_tensor.SparseTensorValue(
            *[ConstantOf(x) for x in truth]),
        normalize=normalize,
        expected_output=expected_output,
        expected_shape=expected_shape,
        expected_err_re=expected_err_re)

# SparseTensor inputs.
with ops.Graph().as_default() as g, self.session(g):
    # hypothesis and truth are (index, value, shape) tuples
    self._testEditDistanceST(
        hypothesis_st=sparse_tensor.SparseTensor(
            *[ConstantOf(x) for x in hypothesis]),
        truth_st=sparse_tensor.SparseTensor(*[ConstantOf(x) for x in truth]),
        normalize=normalize,
        expected_output=expected_output,
        expected_shape=expected_shape,
        expected_err_re=expected_err_re)
