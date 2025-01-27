# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_array_ops_test.py
int_values = np.arange(-3, 3).tolist()
float_values = np.arange(-3.5, 3.5).tolist()
all_values = int_values + float_values
for dtype in self.all_types:
    for start in all_values:
        msg = 'dtype:{} start:{}'.format(dtype, start)
        self.match(np_array_ops.arange(start), np.arange(start), msg=msg)
        self.match(
            np_array_ops.arange(start, dtype=dtype),
            np.arange(start, dtype=dtype),
            msg=msg)
        for stop in all_values:
            msg = 'dtype:{} start:{} stop:{}'.format(dtype, start, stop)
            self.match(
                np_array_ops.arange(start, stop), np.arange(start, stop), msg=msg)
            # TODO(srbs): Investigate and remove check.
            # There are some bugs when start or stop is float and dtype is int.
            if not isinstance(start, float) and not isinstance(stop, float):
                self.match(
                    np_array_ops.arange(start, stop, dtype=dtype),
                    np.arange(start, stop, dtype=dtype),
                    msg=msg)
            # Note: We intentionally do not test with float values for step
            # because numpy.arange itself returns inconsistent results. e.g.
            # np.arange(0.5, 3, step=0.5, dtype=int) returns
            # array([0, 1, 2, 3, 4])
            for step in int_values:
                msg = 'dtype:{} start:{} stop:{} step:{}'.format(
                    dtype, start, stop, step)
                if not step:
                    with self.assertRaises(ValueError):
                        self.match(
                            np_array_ops.arange(start, stop, step),
                            np.arange(start, stop, step),
                            msg=msg)
                        if not isinstance(start, float) and not isinstance(stop, float):
                            self.match(
                                np_array_ops.arange(start, stop, step, dtype=dtype),
                                np.arange(start, stop, step, dtype=dtype),
                                msg=msg)
                else:
                    self.match(
                        np_array_ops.arange(start, stop, step),
                        np.arange(start, stop, step),
                        msg=msg)
                    if not isinstance(start, float) and not isinstance(stop, float):
                        self.match(
                            np_array_ops.arange(start, stop, step, dtype=dtype),
                            np.arange(start, stop, step, dtype=dtype),
                            msg=msg)
