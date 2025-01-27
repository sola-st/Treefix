# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
"""Gets new NodeDefs written by the NodeFileWriter.

    Returns:
      A list of new NodeDefs in the file written by NodeDefWriter since the last
      time this method was called.
    """
node_def_bytes = self.node_file.read()
node_defs = []
cur_pos = 0
while cur_pos < len(node_def_bytes):
    size_bytes = node_def_bytes[cur_pos:cur_pos + 8]
    (size,) = struct.unpack('<Q', size_bytes)
    cur_pos += 8
    node_def = node_def_pb2.NodeDef()
    node_def.ParseFromString(node_def_bytes[cur_pos:cur_pos + size])
    # When running eager op as function is enabled we expect these extra nodes
    # to show up in the list of executed nodes.
    ignored_ops = []
    if context.run_eager_op_as_function_enabled():
        ignored_ops.extend(['_Arg', '_Retval', 'NoOp'])
        # TODO(b/206047926): Fix or remove _Recv/_HostRecv from the ignored_ops.
        ignored_ops.extend(['_Recv', '_HostRecv'])
    if node_def.op not in ignored_ops:
        node_defs.append(node_def)
    cur_pos += size
self.assertEqual(cur_pos, len(node_def_bytes))
exit(node_defs)
