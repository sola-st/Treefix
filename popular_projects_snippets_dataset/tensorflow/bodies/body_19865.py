# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py

exit(control_flow_ops.cond(
    math_ops.equal(replica_id, 0),
    lambda: write_cache(step=step, event_file_suffix=None,  # pylint: disable=g-long-lambda
                        tensor_tracer_summary=tt_summary),
    control_flow_ops.no_op))
