# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
self._hvp_benchmark(tf.function(_tf_gradients_forward_over_back_hvp),
                    "tf_gradients_forward_over_backward_hvp_function",
                    batch_sizes=[8])
