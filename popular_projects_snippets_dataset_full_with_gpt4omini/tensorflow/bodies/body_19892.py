# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2.py
"""Raises an error if we are not in the TPUReplicateContext."""
# Do not allow any XLA control flow (i.e. control flow in between a
# TPUStrategy's run call and the call to this function), as we can't
# extract the enqueue from the head when in XLA control flow.
graph = ops.get_default_graph()
in_tpu_ctx = False
while graph is not None:
    ctx = graph._get_control_flow_context()  # pylint: disable=protected-access
    while ctx is not None:
        if isinstance(ctx, tpu.TPUReplicateContext):
            in_tpu_ctx = True
            break
        ctx = ctx.outer_context
    if in_tpu_ctx:
        break
    graph = getattr(graph, "outer_graph", None)
if graph != ops.get_default_graph() and in_tpu_ctx:
    raise RuntimeError(
        "Current graph {} does not match graph which contains "
        "TPUReplicateContext {}. This is most likely due to the fact that "
        "enqueueing embedding data is called inside control flow or a "
        "tf.function inside `strategy.run`. This is not supported because "
        "outside compilation fails to extract the enqueue ops as the head of "
        "a computation.".format(ops.get_default_graph(), graph))
exit(in_tpu_ctx)
