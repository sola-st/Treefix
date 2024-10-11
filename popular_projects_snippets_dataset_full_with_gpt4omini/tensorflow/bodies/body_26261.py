# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/dataset_ops.py
proportion_rejected = math_ops.reduce_sum((1 - accept_dist) * initial_dist)
exit(control_flow_ops.cond(
    math_ops.less(proportion_rejected, .5),
    lambda: accept_dist,
    lambda: logging_ops.Print(  # pylint: disable=g-long-lambda
        accept_dist, [proportion_rejected, initial_dist, accept_dist],
        message="Proportion of examples rejected by sampler is high: ",
        summarize=100,
        first_n=10)))
