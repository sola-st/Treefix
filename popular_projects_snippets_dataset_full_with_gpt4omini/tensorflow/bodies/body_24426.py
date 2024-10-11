# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/session_debug_testlib.py
run_options = config_pb2.RunOptions(output_partition_graphs=True)
debug_utils.watch_graph(
    run_options, sess.graph, debug_urls=concurrent_debug_urls[index])
for _ in range(100):
    sess.run(incs[index], options=run_options)
