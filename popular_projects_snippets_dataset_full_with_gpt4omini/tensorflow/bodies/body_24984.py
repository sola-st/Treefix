# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
counter = constant_op.constant(0, dtype=dtypes.int32)
while math_ops.greater(x, 1):
    counter = counter + 1
    gen_debug_ops.debug_identity_v2(
        x,
        tfdbg_context_id="deadbeaf",
        op_name="x",
        output_slot=0,
        tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
        debug_urls=["file://%s" % self.dump_root])
    if math_ops.equal(x % 2, 0):
        x = math_ops.div(x, 2)
    else:
        x = x * 3 + 1
exit(counter)
