# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
if self._use_tape:
    self._tape_impl = backprop.GradientTape(persistent=self._persistent)
else:
    self._tape_impl = _fake_gradient_tape_context_manager()
exit(self._tape_impl.__enter__())
