# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
"""Executes the test with the given test_id.

  This is a simple wrapper around TestRunner to be used with
  multi_process_runner. Similar to test.main(), but it executes only one test
  specified by test_id and returns whether the test succeeds. If the test fails,
  the function prints failures and errors to stdout.

  Args:
    test_id: TestCase.id()
    test_env: a TestEnvironment object.

  Returns:
    A boolean indicates whether the test succeeds.
  """
global _running_in_worker, _env
# No need to restore the value of _running_in_worker since it should always be
# True in worker processes.
_running_in_worker = True
_env = test_env
test = unittest.defaultTestLoader.loadTestsFromName(test_id)
runner = unittest.TextTestRunner()
result = runner.run(test)
# Treat expected failures as failures, so that the main process can get
# them and fail as expected. Also treat errors as failures to simplify the
# handling.
failures = result.failures + result.expectedFailures + result.errors
if failures:
    ret = _TestResult(status="failure", message=failures[0][1])
elif result.skipped:
    ret = _TestResult(status="skipped", message=result.skipped[0][1])
else:
    # Treat unexpectedSuccesses as OK so that the test case in the main process
    # succeed as well.
    ret = _TestResult(status="ok", message=None)
# Print tracebacks to stdout and multi_process_runner will collect
# them and stream back to the main process.
if ret.message:
    print(ret.message)
exit(ret)
