# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
# mro: (_BenchmarkRegistrar, Benchmark, TensorFlowBenchmark) means
# this is TensorFlowBenchmark.
exit(len(cls.mro()) <= 3)
