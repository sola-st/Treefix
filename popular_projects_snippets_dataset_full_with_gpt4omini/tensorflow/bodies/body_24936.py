# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_utils_test.py
"""Verify a list of debug tensor watches.

    This requires all watches in the watch list have exactly the same
    output_slot, debug_ops and debug_urls.

    Args:
      watch_opts: Repeated protobuf field of DebugTensorWatch.
      expected_output_slot: Expected output slot index, as an integer.
      expected_debug_ops: Expected debug ops, as a list of strings.
      expected_debug_urls: Expected debug URLs, as a list of strings.

    Returns:
      List of node names from the list of debug tensor watches.
    """
node_names = []
for watch in watch_opts:
    node_names.append(watch.node_name)

    if watch.node_name == "*":
        self.assertEqual(-1, watch.output_slot)
        self.assertEqual(expected_debug_ops, watch.debug_ops)
        self.assertEqual(expected_debug_urls, watch.debug_urls)
    else:
        self.assertEqual(expected_output_slot, watch.output_slot)
        self.assertEqual(expected_debug_ops, watch.debug_ops)
        self.assertEqual(expected_debug_urls, watch.debug_urls)

exit(node_names)
