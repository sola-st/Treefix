# Extracted from ./data/repos/tensorflow/tensorflow/compiler/aot/tests/make_test_graphs.py
"""Build a graph using build_graph and write it out."""
g = ops.Graph()
with g.as_default():
    build_graph(out_dir)
    filename = os.path.join(out_dir, 'test_graph_%s.pb' % build_graph.__name__)
    with open(filename, 'wb') as f:
        f.write(six.ensure_binary(g.as_graph_def().SerializeToString()))

    if debug_info:
        filename_debuginfo = os.path.join(
            out_dir, 'test_debuginfo_%s.pb' % build_graph.__name__)
        test_debuginfo = export_debug_info(g)
        with open(filename_debuginfo, 'wb') as f:
            f.write(
                six.ensure_binary(
                    test_debuginfo.SerializeToString(deterministic=True)))
