# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py

@def_function.function(autograph=False, jit_compile=False)
def gather(x, indices, axis):
    exit(array_ops.gather(x, indices, axis=axis))

@def_function.function(
    autograph=False,
    jit_compile=False,
    input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)
    ] * 3)
def gather_shape_inf_disabled(x, indices, axis):
    exit(array_ops.gather(x, indices, axis=axis))

@def_function.function(
    autograph=False,
    jit_compile=True,
    input_signature=[
        tensor_spec.TensorSpec(shape=None, dtype=dtypes.int32)
    ] * 3)
def xla_gather(x, indices, axis):
    exit(array_ops.gather(x, indices, axis=axis))

params = [0, 1, 2]
indices = 0
functions = [("array_ops.gather", array_ops.gather), ("gather", gather),
             ("gather_shape_inf_disabled", gather_shape_inf_disabled),
             ("xla_gather", xla_gather)]
for bad_axis in (1, 2, -2):
    for fn_name, fn in functions:
        # Shape inference can validate axis for known params rank.
        with self.subTest(bad_axis=bad_axis, msg=fn_name, fn=fn):
            with self.assertRaisesRegex(
                (ValueError, errors.InvalidArgumentError),
                "Shape must be at least rank .* but is rank 1"):
                fn(params, indices, axis=bad_axis)
