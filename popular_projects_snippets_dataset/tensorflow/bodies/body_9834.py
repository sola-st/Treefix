# Extracted from ./data/repos/tensorflow/tensorflow/python/dlpack/dlpack_test.py
np.random.seed(42)
np_array = np.random.randint(0, 10, (2, 3, 4))
tf_tensor = constant_op.constant(np_array, dtype=np.float32)
dlcapsule = dlpack.to_dlpack(tf_tensor)
del tf_tensor  # should still work
_ = dlpack.from_dlpack(dlcapsule)

def ConsumeDLPackTensor():
    dlpack.from_dlpack(dlcapsule)  # Should can be consumed only once

self.assertRaisesRegex(Exception,
                       ".*a DLPack tensor may be consumed at most once.*",
                       ConsumeDLPackTensor)
