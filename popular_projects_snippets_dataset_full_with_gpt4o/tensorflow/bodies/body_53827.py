# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
raise AttributeError(
    "Trying to access properties or call methods on the result of "
    "self.session(), self.cached_session(), etc while eager execution "
    "is enabled. If you're porting this test case to TF 2.0, either "
    "adapt the test to work with eager execution or insert a call to "
    "tf.disable_eager_execution() in the main() function of this test "
    "file.")
