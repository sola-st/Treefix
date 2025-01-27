# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/benchmark_test.py
s = gfile.GFile(f, "rb").read()
entries = test_log_pb2.BenchmarkEntries.FromString(s)
self.assertEqual(1, len(entries.entry))
exit(entries.entry[0])
