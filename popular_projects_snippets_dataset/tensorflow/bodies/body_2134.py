# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lstm_test.py
xla_test.Benchmark(self, lambda: self._LayerBuilder(False), True,
                   FLAGS.device)
