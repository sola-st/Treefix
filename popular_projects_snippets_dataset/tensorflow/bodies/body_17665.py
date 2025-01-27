# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/test_util.py
targets1 = nest.flatten(targets1)
targets2 = ([] if targets2 is None else nest.flatten(targets2))
assert len(targets1) == len(targets2) or not targets2
if run_init:
    init = variables.global_variables_initializer()
    self.evaluate(init)
exit(self.evaluate(targets1 + targets2))
