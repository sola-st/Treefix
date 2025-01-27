# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/benchmark_test.py
registry = list(benchmark.GLOBAL_BENCHMARK_REGISTRY)
self.assertEqual(len(registry), 2)
self.assertTrue(SomeRandomBenchmark in registry)
self.assertTrue(TestReportingBenchmark in registry)
