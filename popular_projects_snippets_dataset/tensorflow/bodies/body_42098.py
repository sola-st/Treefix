# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
self._hvp_benchmark(_back_over_forward_hvp,
                    "backward_over_forward_hvp_eager",
                    batch_sizes=[8])
