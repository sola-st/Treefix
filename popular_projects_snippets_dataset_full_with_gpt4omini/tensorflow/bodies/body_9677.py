# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
with session.Session():
    for shape in [(32, 4, 128), (37,), (2, 0, 6), (0, 0, 0)]:
        size = 1
        for s in shape:
            size *= s
        c_list = np.array([compat.as_bytes(str(i)) for i in range(size)],
                          dtype=np.object_).reshape(shape) if size > 0 else []
        c = constant_op.constant(c_list)
        self.assertAllEqual(c, c_list)
