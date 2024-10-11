# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/benchmarks/resnet50/hvp_test.py
self._hvp_benchmark(_forward_over_back_hvp,
                    "forward_over_backward_hvp_eager",
                    batch_sizes=[8])
