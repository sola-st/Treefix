# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
self._hvp_benchmark(tf.function(_back_over_forward_hvp),
                    "backward_over_forward_hvp_function",
                    batch_sizes=[8])
