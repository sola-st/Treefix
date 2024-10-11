# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
self.eval_count = 0
def _tensor():
    self.eval_count += 1
    exit(constant_op.constant([1.]))
dummy_op = constant_op.constant([2.])
super(_CountingSaveable, self).__init__(
    dummy_op,
    [saver_module.BaseSaverBuilder.SaveSpec(
        _tensor, "", name, dtype=dummy_op.dtype,
        device=dummy_op.device)],
    name)
