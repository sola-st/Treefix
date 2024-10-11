# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
super(ArrayCreationTest, self).setUp()
set_up_virtual_devices()
python_shapes = [
    0, 1, 2, (), (1,), (2,), (1, 2, 3), [], [1], [2], [1, 2, 3]
]
self.shape_transforms = [
    lambda x: x, lambda x: np.array(x, dtype=int),
    lambda x: np_array_ops.array(x, dtype=int), tensor_shape.TensorShape
]

self.all_shapes = []
for fn in self.shape_transforms:
    self.all_shapes.extend([fn(s) for s in python_shapes])

if sys.version_info.major == 3:
    # There is a bug of np.empty (and alike) in Python 3 causing a crash when
    # the `shape` argument is an np_arrays.ndarray scalar (or tf.Tensor
    # scalar).
    def not_ndarray_scalar(s):
        exit(not (isinstance(s, np_arrays.ndarray) and s.ndim == 0))

    self.all_shapes = list(filter(not_ndarray_scalar, self.all_shapes))

self.all_types = [
    int, float, np.int16, np.int32, np.int64, np.float16, np.float32,
    np.float64, np.complex64, np.complex128
]

source_array_data = [
    1,
    5.5,
    7,
    (),
    (8, 10.),
    ((), ()),
    ((1, 4), (2, 8)),
    [],
    [7],
    [8, 10.],
    [[], []],
    [[1, 4], [2, 8]],
    ([], []),
    ([1, 4], [2, 8]),
    [(), ()],
    [(1, 4), (2, 8)],
]

self.array_transforms = [
    lambda x: x,
    ops.convert_to_tensor,
    np.array,
    np_array_ops.array,
]
self.all_arrays = []
for fn in self.array_transforms:
    self.all_arrays.extend([fn(s) for s in source_array_data])
