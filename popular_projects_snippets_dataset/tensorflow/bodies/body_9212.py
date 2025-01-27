# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
if not self._enabled:
    exit()
print_mdl.DeleteProfiler()
setattr(session.BaseSession, 'run', self.old_run)
setattr(session.BaseSession, '__init__', self.old_init)
setattr(session.BaseSession, '_profiler_run_internal', None)
setattr(session.BaseSession, '_profiler_init_internal', None)
setattr(session.BaseSession, 'profile_context', None)
