# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir.py
"""Generate the Compiler Ir from tf concrete function.

  Args:
    concrete_fn: returned by using get_concrete_function.

  Returns:
    Function callable that generate the HLO text.

  Raises:
      ValueError: if concrete_fn is not "compilable" without concrete
      inputs.
  """
context.ensure_initialized()
# TODO(b/265073174) support users input tf.TensorSpec list here.
if not all(
    [s.shape.is_fully_defined() for s in nest.flatten(concrete_fn.inputs)]
):
    raise ValueError(
        f"Only support static input shape but got inputs = {concrete_fn.inputs}"
    )
fn_name = concrete_fn.name

def compiler_ir_generator(stage="hlo", device_name=None):
    device_name = maybe_get_device_name(device_name)
    res_bytes = context.context().get_compiler_ir(
        device_name=device_name,
        stage=stage,
        function_name=fn_name,
        # args list is empty for using_tensor_spec case
        args=[],
    )
    if stage in (
        "hlo_serialized",
        "optimized_hlo_serialized",
        "optimized_hlo_proto_serialized",
    ):
        exit(res_bytes)
    else:
        exit(res_bytes.decode("utf-8"))

exit(compiler_ir_generator)
