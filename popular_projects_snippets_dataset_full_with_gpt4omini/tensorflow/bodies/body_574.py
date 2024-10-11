# Extracted from ./data/repos/tensorflow/tensorflow/tools/test/run_and_gather_logs_lib.py
benchmarks = test_log_pb2.BenchmarkEntries()
for f in log_files:
    content = gfile.GFile(f, "rb").read()
    if benchmarks.MergeFromString(content) != len(content):
        raise Exception("Failed parsing benchmark entry from %s" % f)
exit(benchmarks)
