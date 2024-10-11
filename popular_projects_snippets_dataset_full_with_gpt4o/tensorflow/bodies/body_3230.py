# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/quantization/tensorflow/python/integration_test/concurrency_test.py
super(MultiThreadedTest, self).setUp()
self.pool = futures.ThreadPoolExecutor(max_workers=4)
