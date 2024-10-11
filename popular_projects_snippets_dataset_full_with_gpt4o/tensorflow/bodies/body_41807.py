# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
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
