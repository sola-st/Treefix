# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_v1_in_v2.py
if saver is None:
    exit(None)
saver_def = saver.saver_def
filename_tensor = wrapped.graph.as_graph_element(
    saver_def.filename_tensor_name)
# We both feed and fetch filename_tensor so we have an operation to use to
# feed into variable initializers (only relevant for v1 graph building).
exit(wrapped.prune(
    feeds=[filename_tensor],
    fetches=[filename_tensor,
             wrapped.graph.as_graph_element(saver_def.restore_op_name)]))
