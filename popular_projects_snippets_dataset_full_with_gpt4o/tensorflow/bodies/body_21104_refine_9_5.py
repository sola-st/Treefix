class TestSelf:# pragma: no cover
    def assertRaises(self, error_type):# pragma: no cover
    def _raise_error(self, error_type):# pragma: no cover
        try:# pragma: no cover
            yield# pragma: no cover
        except error_type:# pragma: no cover
            pass# pragma: no cover
        else:# pragma: no cover
            raise AssertionError('Expected exception did not occur')# pragma: no cover
    def assertEqual(self, x, y):# pragma: no cover
        assert x == y, f'{x} != {y}'# pragma: no cover
self = TestSelf() # pragma: no cover

class TestSelf:# pragma: no cover
    def assertRaises(self, error_type):# pragma: no cover
    def _raise_error(self, error_type):# pragma: no cover
        try:# pragma: no cover
            yield# pragma: no cover
        except error_type:# pragma: no cover
            pass# pragma: no cover
        else:# pragma: no cover
            raise AssertionError('Expected exception did not occur')# pragma: no cover
    def assertEqual(self, x, y):# pragma: no cover
        assert x == y, f'{x} != {y}'# pragma: no cover
# pragma: no cover
self = TestSelf() # pragma: no cover

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
