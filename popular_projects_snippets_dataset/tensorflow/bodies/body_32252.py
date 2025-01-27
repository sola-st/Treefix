# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/unicode_script_op_test.py
with session.Session(config=benchmark.benchmark_config()) as sess:
    chars = self._generateBenchmarkInput(1000000)
    script = string_ops.unicode_script(chars)
    self.run_op_benchmark(sess, script.op, min_iters=100)
