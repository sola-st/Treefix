# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x: 2. * x[0],
    input_signature=([
        tensor_spec.TensorSpec(None, dtypes.float32),
        tensor_spec.TensorSpec(None, dtypes.float32)
    ],))
root.f([constant_op.constant(1.), constant_op.constant(1.)])
