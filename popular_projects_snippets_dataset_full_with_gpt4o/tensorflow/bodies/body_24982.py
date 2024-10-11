# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
square = math_ops.square(x)
gen_debug_ops.debug_identity_v2(
    square,
    tfdbg_context_id="deadbeaf",
    op_name="Square",
    output_slot=0,
    tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
    debug_urls=["file://%s" % self.dump_root])

sqrt = math_ops.sqrt(x)
gen_debug_ops.debug_identity_v2(
    sqrt,
    tfdbg_context_id="beafdead",
    op_name="Sqrt",
    output_slot=0,
    tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
    debug_urls=["file://%s" % self.dump_root])
exit(square + sqrt)
