# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
super(SingleWorkerTest, self).tearDown()

# Clear the current device scope to avoid polluting other test cases.
ops.device(None).__enter__()
# Reset the context to avoid polluting other test cases.
context._reset_context()
