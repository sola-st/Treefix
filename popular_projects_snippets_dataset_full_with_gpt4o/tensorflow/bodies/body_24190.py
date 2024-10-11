# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/framework_test.py
"""Constructor.

    Args:
      sess: The TensorFlow Session object to be wrapped.
      bad_init_action: (str) bad action value to be returned during the
        on-session-init callback.
      bad_run_start_action: (str) bad action value to be returned during the
        the on-run-start callback.
      bad_debug_urls: Bad URL values to be returned during the on-run-start
        callback.
    """

self._bad_init_action = bad_init_action
self._bad_run_start_action = bad_run_start_action
self._bad_debug_urls = bad_debug_urls

# Invoke superclass constructor.
framework.BaseDebugWrapperSession.__init__(self, sess)
