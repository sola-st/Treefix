import unittest # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def assertEqual(self, first, second, msg=None): # pragma: no cover
        if first != second: # pragma: no cover
            raise AssertionError(msg or f'{first} != {second}') # pragma: no cover
    def assertRaises(self, expected_exception): # pragma: no cover
        class ContextManager: # pragma: no cover
            def __enter__(self): # pragma: no cover
                return self # pragma: no cover
            def __exit__(self, exc_type, exc_value, traceback): # pragma: no cover
                if not exc_type or not issubclass(exc_type, expected_exception): # pragma: no cover
                    raise AssertionError(f'{expected_exception} not raised') # pragma: no cover
                return True # pragma: no cover
        return ContextManager() # pragma: no cover
mock_test_case = MockTestCase() # pragma: no cover
self = type('Mock', (object,), { # pragma: no cover
    'assertRaises': mock_test_case.assertRaises, # pragma: no cover
    'assertEqual': mock_test_case.assertEqual # pragma: no cover
})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(21667)

    gstep = training_util.get_or_create_global_step()
    _l_(21657)

    class _RaiseAbortedHook(session_run_hook.SessionRunHook):
        _l_(21660)


        def before_run(self, run_context):
            _l_(21659)

            raise errors_impl.AbortedError(None, None, 'Abort')
            _l_(21658)

    with monitored_session.SingularMonitoredSession(
        hooks=[_RaiseAbortedHook()]) as session:
        _l_(21663)

        with self.assertRaises(errors_impl.AbortedError):
            _l_(21662)

            self.assertEqual(0, session.run(gstep))
            _l_(21661)

    with self.assertRaises(errors_impl.AbortedError):
        _l_(21666)

        with monitored_session.SingularMonitoredSession(
            hooks=[_RaiseAbortedHook()]) as session:
            _l_(21665)

            self.assertEqual(0, session.run(gstep))
            _l_(21664)
