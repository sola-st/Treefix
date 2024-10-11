# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util_test.py
# test plain int
self.assertAllCloseAccordingToType(1, 1, rtol=1e-8, atol=1e-8)

# test float64
self.assertAllCloseAccordingToType(
    np.asarray([1e-8], dtype=np.float64),
    np.asarray([2e-8], dtype=np.float64),
    rtol=1e-8, atol=1e-8
)

self.assertAllCloseAccordingToType(
    constant_op.constant([1e-8], dtype=dtypes.float64),
    constant_op.constant([2e-8], dtype=dtypes.float64),
    rtol=1e-8,
    atol=1e-8)

with (self.assertRaises(AssertionError)):
    self.assertAllCloseAccordingToType(
        np.asarray([1e-7], dtype=np.float64),
        np.asarray([2e-7], dtype=np.float64),
        rtol=1e-8, atol=1e-8
    )

# test float32
self.assertAllCloseAccordingToType(
    np.asarray([1e-7], dtype=np.float32),
    np.asarray([2e-7], dtype=np.float32),
    rtol=1e-8, atol=1e-8,
    float_rtol=1e-7, float_atol=1e-7
)

self.assertAllCloseAccordingToType(
    constant_op.constant([1e-7], dtype=dtypes.float32),
    constant_op.constant([2e-7], dtype=dtypes.float32),
    rtol=1e-8,
    atol=1e-8,
    float_rtol=1e-7,
    float_atol=1e-7)

with (self.assertRaises(AssertionError)):
    self.assertAllCloseAccordingToType(
        np.asarray([1e-6], dtype=np.float32),
        np.asarray([2e-6], dtype=np.float32),
        rtol=1e-8, atol=1e-8,
        float_rtol=1e-7, float_atol=1e-7
    )

# test float16
self.assertAllCloseAccordingToType(
    np.asarray([1e-4], dtype=np.float16),
    np.asarray([2e-4], dtype=np.float16),
    rtol=1e-8, atol=1e-8,
    float_rtol=1e-7, float_atol=1e-7,
    half_rtol=1e-4, half_atol=1e-4
)

self.assertAllCloseAccordingToType(
    constant_op.constant([1e-4], dtype=dtypes.float16),
    constant_op.constant([2e-4], dtype=dtypes.float16),
    rtol=1e-8,
    atol=1e-8,
    float_rtol=1e-7,
    float_atol=1e-7,
    half_rtol=1e-4,
    half_atol=1e-4)

with (self.assertRaises(AssertionError)):
    self.assertAllCloseAccordingToType(
        np.asarray([1e-3], dtype=np.float16),
        np.asarray([2e-3], dtype=np.float16),
        rtol=1e-8, atol=1e-8,
        float_rtol=1e-7, float_atol=1e-7,
        half_rtol=1e-4, half_atol=1e-4
    )
