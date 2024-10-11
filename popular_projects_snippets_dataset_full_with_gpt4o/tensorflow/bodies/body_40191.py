# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_execution_test.py
super(RemoteExecutionTest, self).tearDown()

# Clear the current device scope and reset the context to avoid polluting
# other test cases.
ops.device(None).__enter__()
context._reset_context()
