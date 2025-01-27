# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
with writer.as_default():
    with summary_ops.record_if(True):
        summary_ops.scalar("result", step * const_multiple, step=step)
        step.assign_add(1)
