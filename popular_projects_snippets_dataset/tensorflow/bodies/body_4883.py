# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
exit(control_flow_ops.group(
    [self.v.assign(v_new), self.w.assign(w_new)]))
