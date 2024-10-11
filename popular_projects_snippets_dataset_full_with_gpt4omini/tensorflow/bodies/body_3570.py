# Extracted from ./data/repos/tensorflow/tensorflow/core/function/transform/transform_test.py
m = Model()
# Originally f does addition
self.assertEqual(
    m.f(
        constant_op.constant(1, dtypes.int32),
        constant_op.constant(2, dtypes.int32),
        constant_op.constant(False, dtypes.bool)), 3)

self.assertEqual(
    m.f(
        constant_op.constant(1, dtypes.int32),
        constant_op.constant(2, dtypes.int32),
        constant_op.constant(True, dtypes.bool)), 5)

# Transform every input signature of f to a multiply
m.f = apply_transform(m.f, add_to_multiply)

# Validate arbitrary signatures.
self.assertEqual(
    m.f(
        constant_op.constant(1, dtypes.int32),
        constant_op.constant(2, dtypes.int32),
        constant_op.constant(False, dtypes.bool)), 2)
self.assertEqual(
    m.f(
        constant_op.constant(1, dtypes.int32),
        constant_op.constant(2, dtypes.int32),
        constant_op.constant(True, dtypes.bool)), 4)
self.assertEqual(
    m.f(
        constant_op.constant(1.0, dtypes.float32),
        constant_op.constant(2.0, dtypes.float32),
        constant_op.constant(False, dtypes.bool)), (2.0))

# Save and restore the model.
save_lib.save(m, "/tmp/testing_model")
m_loaded = load_lib.load("/tmp/testing_model")

# Validate the restored model.
self.assertEqual(
    m_loaded.f(
        constant_op.constant(1, dtypes.int32),
        constant_op.constant(2, dtypes.int32),
        constant_op.constant(False, dtypes.bool)), 2)
self.assertEqual(
    m_loaded.f(
        constant_op.constant(1.1, dtypes.float32),
        constant_op.constant(2.0, dtypes.float32),
        constant_op.constant(True, dtypes.bool)), (4.2))
