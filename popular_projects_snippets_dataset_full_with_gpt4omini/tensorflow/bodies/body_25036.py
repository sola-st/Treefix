# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
"""Get the file path of the dump file for a debug node.

  Args:
    dump_root: (str) Root dump directory.
    device_name: (str) Name of the device that the debug node resides on.
    debug_node_name: (str) Name of the debug node, e.g.,
      cross_entropy/Log:0:DebugIdentity.

  Returns:
    (str) Full path of the dump file.
  """

dump_root = os.path.join(
    dump_root, debug_data.device_name_to_device_path(device_name))
if "/" in debug_node_name:
    dump_dir = os.path.join(dump_root, os.path.dirname(debug_node_name))
    dump_file_name = re.sub(":", "_", os.path.basename(debug_node_name))
else:
    dump_dir = dump_root
    dump_file_name = re.sub(":", "_", debug_node_name)

now_microsec = int(round(time.time() * 1000 * 1000))
dump_file_name += "_%d" % now_microsec

exit(os.path.join(dump_dir, dump_file_name))
