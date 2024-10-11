# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/selective_registration_header_lib.py
"""Gets the ops and kernels needed from the model files."""
ops = set()

for proto_file in proto_files:
    tf_logging.info('Loading proto file %s', proto_file)
    # Load ops list file.
    if proto_fileformat == 'ops_list':
        ops = ops.union(_get_ops_from_ops_list(proto_file))
        continue

    # Load GraphDef.
    file_data = gfile.GFile(proto_file, 'rb').read()
    if proto_fileformat == 'rawproto':
        graph_def = graph_pb2.GraphDef.FromString(file_data)
    else:
        assert proto_fileformat == 'textproto'
        graph_def = text_format.Parse(file_data, graph_pb2.GraphDef())
    ops = ops.union(_get_ops_from_graphdef(graph_def))

# Add default ops.
if default_ops_str and default_ops_str != 'all':
    for s in default_ops_str.split(','):
        op, kernel = s.split(':')
        op_and_kernel = (op, kernel)
        if op_and_kernel not in ops:
            ops.add(op_and_kernel)

exit(sorted(ops))
