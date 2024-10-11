# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/benchmark_test.py
# Validate that SomeBenchmark has not run yet
self.assertFalse(_ran_somebenchmark_1[0])
self.assertFalse(_ran_somebenchmark_2[0])
self.assertFalse(_ran_somebenchmark_but_shouldnt[0])

# Run other benchmarks, but this wont run the one we care about
with self.assertRaises(ValueError):
    benchmark._run_benchmarks("unrelated")

# Validate that SomeBenchmark has not run yet
self.assertFalse(_ran_somebenchmark_1[0])
self.assertFalse(_ran_somebenchmark_2[0])
self.assertFalse(_ran_somebenchmark_but_shouldnt[0])

# Run all the benchmarks, avoid generating any reports
if benchmark.TEST_REPORTER_TEST_ENV in os.environ:
    del os.environ[benchmark.TEST_REPORTER_TEST_ENV]
benchmark._run_benchmarks("SomeRandom")

# Validate that SomeRandomBenchmark ran correctly
self.assertTrue(_ran_somebenchmark_1[0])
self.assertTrue(_ran_somebenchmark_2[0])
self.assertFalse(_ran_somebenchmark_but_shouldnt[0])

_ran_somebenchmark_1[0] = False
_ran_somebenchmark_2[0] = False
_ran_somebenchmark_but_shouldnt[0] = False

# Test running a specific method of SomeRandomBenchmark
if benchmark.TEST_REPORTER_TEST_ENV in os.environ:
    del os.environ[benchmark.TEST_REPORTER_TEST_ENV]
benchmark._run_benchmarks("SomeRandom.*1$")

self.assertTrue(_ran_somebenchmark_1[0])
self.assertFalse(_ran_somebenchmark_2[0])
self.assertFalse(_ran_somebenchmark_but_shouldnt[0])
