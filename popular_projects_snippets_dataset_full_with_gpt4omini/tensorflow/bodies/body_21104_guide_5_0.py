def get_or_create_global_step(): return gstep # pragma: no cover
self = type('Mock', (object,), {})() # pragma: no cover
self.assertEqual = lambda x, y: None # pragma: no cover
self.assertRaises = lambda exc: (lambda f: f())(lambda: (_ for _ in ()).throw(exc)) # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
from l3.Runtime import _l_
with ops.Graph().as_default():
    _l_(9348)

    gstep = training_util.get_or_create_global_step()
    _l_(9338)

    class _RaiseAbortedHook(session_run_hook.SessionRunHook):
        _l_(9341)


        def before_run(self, run_context):
            _l_(9340)

            raise errors_impl.AbortedError(None, None, 'Abort')
            _l_(9339)

    with monitored_session.SingularMonitoredSession(
        hooks=[_RaiseAbortedHook()]) as session:
        _l_(9344)

        with self.assertRaises(errors_impl.AbortedError):
            _l_(9343)

            self.assertEqual(0, session.run(gstep))
            _l_(9342)

    with self.assertRaises(errors_impl.AbortedError):
        _l_(9347)

        with monitored_session.SingularMonitoredSession(
            hooks=[_RaiseAbortedHook()]) as session:
            _l_(9346)

            self.assertEqual(0, session.run(gstep))
            _l_(9345)
