# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/testdata/gen_tf_readvariableop_model.py
"""Generate a model with ReadVariableOp nodes."""
my_model = MyModel()
cfunc = my_model.__call__.get_concrete_function(
    tensor_spec.TensorSpec([None, 1, 1], dtypes.float32),
    tensor_spec.TensorSpec([None, 1, 1], dtypes.float32))
# pylint: disable=not-callable
save(my_model, tf_saved_model_dir, signatures=cfunc)
