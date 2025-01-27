# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
debug_utils.add_debug_tensor_watch(
    self._run_options,
    "foo/node_a",
    0,
    debug_ops=["DebugNanCount", "DebugIdentity"],
    debug_urls="file:///tmp/tfdbg_1")

debug_watch_opts = self._run_options.debug_options.debug_tensor_watch_opts
self.assertEqual(1, len(debug_watch_opts))

watch_0 = debug_watch_opts[0]

self.assertEqual("foo/node_a", watch_0.node_name)
self.assertEqual(0, watch_0.output_slot)

# Verify default debug op name.
self.assertEqual(["DebugNanCount", "DebugIdentity"], watch_0.debug_ops)

# Verify debug URLs.
self.assertEqual(["file:///tmp/tfdbg_1"], watch_0.debug_urls)
