# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
if context.executing_eagerly():
    self._test_minimize_loss_eager(distribution)
else:
    self._test_minimize_loss_graph(distribution)
