# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/make_aot_compile_models.py
"""Create a SavedModel that performs a large matmul."""
root = autotrackable.AutoTrackable()
root.f = def_function.function(
    lambda x, y: math_ops.matmul(x, y),  # pylint: disable=unnecessary-lambda
    input_signature=[tensor_spec.TensorSpec([3000, 5000], dtypes.float32),
                     tensor_spec.TensorSpec([5000, 4000], dtypes.float32),])
root.f(x=array_ops.zeros((3000, 5000)),
       y=array_ops.zeros((5000, 4000)))
save_dir = os.path.join(out_dir, 'x_matmul_y_large')
save.save(root, save_dir, root.f)
# This simple SavedModel lacks any variables, but we need to create a
# variables.index file to make bazel genrule happy.
with open(os.path.join(save_dir, 'variables', 'variables.index'), 'w'):
    pass
