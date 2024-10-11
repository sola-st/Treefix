# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
self._hvp_benchmark(tf.function(_back_over_back_hvp),
                    "backward_over_backward_hvp_function",
                    batch_sizes=[8])
