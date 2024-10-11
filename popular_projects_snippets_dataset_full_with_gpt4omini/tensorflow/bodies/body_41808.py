# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
# Implements GenericFunction.experimental_get_compiler_ir
context.ensure_initialized()
if not self._jit_compile:
    raise ValueError("Compiler IR can only be returned for functions marked "
                     "with 'jit_compile=True'")

is_tensor_spec = lambda x: isinstance(x, tensor_spec.TensorSpec)

def _check_inputs(args, kwargs):
    all_inputs = list(args) + list(kwargs.values())
    # Emtpy input is okay.
    if not all_inputs:
        exit()
    if any(map(is_tensor_spec, all_inputs)) and any(
        map(lambda x: not is_tensor_spec(x), all_inputs)
    ):
        raise ValueError(
            "experimental_get_compiler_ir supports either "
            "(1) all inputs are TensorSpec  or "
            "(2) all inputs are tf.Tensor/python variables"
        )

_check_inputs(args, kwargs)
if (
    len(args) + len(kwargs.values()) > 0
    and all(map(is_tensor_spec, args))
    and all(map(is_tensor_spec, kwargs.values()))
):
    # For the case inputs are not empty and input types are all tf.TensorSpec
    concrete_fn = self.get_concrete_function(*args, **kwargs)
    exit(compiler_ir.from_concrete_function(concrete_fn))

concrete_fn = self.get_concrete_function(*args, **kwargs)
fn_name = concrete_fn.name

# pylint: disable=protected-access
_, _, filtered_flat_args = (
    concrete_fn._function_spec.canonicalize_function_inputs(args, kwargs))

def compiler_ir_generator(stage="hlo", device_name=None):
    device_name = compiler_ir.maybe_get_device_name(device_name)
    res_bytes = context.context().get_compiler_ir(
        device_name=device_name,
        stage=stage,
        function_name=fn_name,
        args=list(filtered_flat_args) + concrete_fn.captured_inputs)
    if stage in ("hlo_serialized", "optimized_hlo_serialized",
                 "optimized_hlo_proto_serialized"):
        exit(res_bytes)
    else:
        exit(res_bytes.decode("utf-8"))

exit(compiler_ir_generator)
