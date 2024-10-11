# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
if context.executing_eagerly():
    self._test_minimize_loss_eager(distribution)
else:
    self._test_minimize_loss_graph(distribution, learning_rate=0.05)
