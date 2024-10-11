class MockSelf:# pragma: no cover
    @staticmethod# pragma: no cover
    def assertRaises(*args, **kwargs): pass# pragma: no cover
    @staticmethod# pragma: no cover
    def assertEqual(*args, **kwargs): pass # pragma: no cover
self = MockSelf() # pragma: no cover

class MockSelf:# pragma: no cover
    def assertRaises(self, exc_type, callable_obj=None, *args, **kwargs):# pragma: no cover
        if callable_obj:# pragma: no cover
            with self.assertRaises(exc_type):# pragma: no cover
                return callable_obj(*args, **kwargs)# pragma: no cover
        return self.assertRaises(exc_type)# pragma: no cover
    def assertEqual(self, first, second, msg=None):# pragma: no cover
        assert first == second, msg if msg else f'{first} != {second}' # pragma: no cover
self = MockSelf() # pragma: no cover

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
