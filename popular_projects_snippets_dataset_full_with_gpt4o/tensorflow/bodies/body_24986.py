# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_v2_ops_test.py
# DebugIdentityV2 is a stateful op. It ought to be included by auto
# control dependency.
square = math_ops.square(x)
gen_debug_ops.debug_identity_v2(
    square,
    tfdbg_context_id="deadbeaf",
    tensor_debug_mode=debug_event_pb2.TensorDebugMode.FULL_TENSOR,
    debug_urls=["file://%s" % self.dump_root, another_debug_url])
exit(square + 1.0)
