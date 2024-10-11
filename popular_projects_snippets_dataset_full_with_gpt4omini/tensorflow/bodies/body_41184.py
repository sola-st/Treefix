# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/compiler_ir.py
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
