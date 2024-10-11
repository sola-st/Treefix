# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/data_structures/fifo_queue_test.py
with self.cached_session() as sess:
    dtypes = [
        dtypes_lib.float32, dtypes_lib.float64, dtypes_lib.int32,
        dtypes_lib.uint8, dtypes_lib.int16, dtypes_lib.int8, dtypes_lib.int64,
        dtypes_lib.uint16, dtypes_lib.bool, dtypes_lib.complex64,
        dtypes_lib.complex128
    ]
    shape = (32, 4, 128)
    q = data_flow_ops.FIFOQueue(32, dtypes, [shape[1:]] * len(dtypes))

    input_tuple = []
    for dtype in dtypes:
        np_dtype = dtype.as_numpy_dtype
        np_array = np.random.randint(-10, 10, shape)
        if dtype == dtypes_lib.bool:
            np_array = np_array > 0
        elif dtype in (dtypes_lib.complex64, dtypes_lib.complex128):
            np_array = np.sqrt(np_array.astype(np_dtype))
        else:
            np_array = np_array.astype(np_dtype)
        input_tuple.append(np_array)

    q.enqueue_many(input_tuple).run()

    output_tuple_t = q.dequeue_many(32)
    output_tuple = self.evaluate(output_tuple_t)

    for (input_elem, output_elem) in zip(input_tuple, output_tuple):
        self.assertAllEqual(input_elem, output_elem)
