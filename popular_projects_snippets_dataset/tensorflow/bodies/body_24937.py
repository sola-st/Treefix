# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
debug_utils.add_debug_tensor_watch(
    self._run_options, "foo/node_a", 1, debug_urls="file:///tmp/tfdbg_1")
debug_utils.add_debug_tensor_watch(
    self._run_options, "foo/node_b", 0, debug_urls="file:///tmp/tfdbg_2")

debug_watch_opts = self._run_options.debug_options.debug_tensor_watch_opts
self.assertEqual(2, len(debug_watch_opts))

watch_0 = debug_watch_opts[0]
watch_1 = debug_watch_opts[1]

self.assertEqual("foo/node_a", watch_0.node_name)
self.assertEqual(1, watch_0.output_slot)
self.assertEqual("foo/node_b", watch_1.node_name)
self.assertEqual(0, watch_1.output_slot)
# Verify default debug op name.
self.assertEqual(["DebugIdentity"], watch_0.debug_ops)
self.assertEqual(["DebugIdentity"], watch_1.debug_ops)

# Verify debug URLs.
self.assertEqual(["file:///tmp/tfdbg_1"], watch_0.debug_urls)
self.assertEqual(["file:///tmp/tfdbg_2"], watch_1.debug_urls)
