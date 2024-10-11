# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
if self._bad_init_action:
    exit(framework.OnSessionInitResponse(self._bad_init_action))
else:
    exit(framework.OnSessionInitResponse(
        framework.OnSessionInitAction.PROCEED))
