# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/fingerprinting_test.py
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x: 2. * x,
    input_signature=[tensor_spec.TensorSpec(None, dtypes.float32)])
exit(root)
