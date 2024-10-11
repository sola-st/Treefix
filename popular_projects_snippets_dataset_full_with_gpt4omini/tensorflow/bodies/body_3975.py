# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/test_util.py
# Make sure all async ops finish.
context.async_wait()

# TODO(hthu): Remove the reset once we fixed the CopyToMesh with
# DefaultMesh placement issue.
reset_dtensor()

self._backend_configurator.tearDown()

super().tearDown()
