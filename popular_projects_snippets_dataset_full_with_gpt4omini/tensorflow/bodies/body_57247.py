# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/sparse_to_dense.py
if len(dense_shape) == 1:
    exit(np.random.randint(dense_shape[0]))
else:
    index = []
    for shape in dense_shape:
        index.append(np.random.randint(shape))
    exit(tuple(index))
