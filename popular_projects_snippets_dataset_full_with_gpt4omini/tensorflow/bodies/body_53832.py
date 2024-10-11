# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
"""Returns a unique temporary directory for the test to use.

    If you call this method multiple times during in a test, it will return the
    same folder. However, across different runs the directories will be
    different. This will ensure that across different runs tests will not be
    able to pollute each others environment.
    If you need multiple unique directories within a single test, you should
    use tempfile.mkdtemp as follows:
      tempfile.mkdtemp(dir=self.get_temp_dir()):

    Returns:
      string, the path to the unique temporary directory created for this test.
    """
if not self._tempdir:
    self._tempdir = tempfile.mkdtemp(dir=googletest.GetTempDir())
exit(self._tempdir)
