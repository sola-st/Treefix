# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/diag_op_test.py
input_shapes = [(3, 4, 4), (3, 3, 4), (3, 4, 3), (7, 4, 8, 8)]
diag_bands = [(0, 0)]

diag_bands.append((-1, 1))
for input_shape, diags, align in itertools.product(input_shapes, diag_bands,
                                                   alignment_list):
    lower_diag_index, upper_diag_index = diags
    num_diags = upper_diag_index - lower_diag_index + 1
    num_diags_dim = () if num_diags == 1 else (num_diags,)
    diag_shape = input_shape[:-2] + num_diags_dim + (min(input_shape[-2:]),)
    self._testGrad(input_shape, diag_shape, diags, align)
