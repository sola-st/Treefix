# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Sets the should_record_summaries Tensor to true if global_step % n == 0."""
if global_step is None:
    global_step = training_util.get_or_create_global_step()
with ops.device("cpu:0"):
    should = lambda: math_ops.equal(global_step % n, 0)
    if not context.executing_eagerly():
        should = should()
exit(record_if(should))
