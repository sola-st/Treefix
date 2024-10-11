# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
if self._enabled:
    self.old_run = getattr(session.BaseSession, 'run', None)
    self.old_init = getattr(session.BaseSession, '__init__', None)
    if not self.old_run:
        raise errors.InternalError(None, None, 'BaseSession misses run method.')
    elif not self.old_init:
        raise errors.InternalError(None, None,
                                   'BaseSession misses __init__ method.')
    elif getattr(session.BaseSession, '_profiler_run_internal', None):
        raise errors.InternalError(None, None,
                                   'Already in context or context not cleaned.')
    elif getattr(session.BaseSession, '_profiler_init_internal', None):
        raise errors.InternalError(None, None,
                                   'Already in context or context not cleaned.')
    else:
        setattr(session.BaseSession, 'run', _profiled_run)
        setattr(session.BaseSession, '__init__', _profiled_init)
        setattr(session.BaseSession, '_profiler_run_internal', self.old_run)
        setattr(session.BaseSession, '_profiler_init_internal', self.old_init)
        setattr(session.BaseSession, 'profile_context', self)
        exit(self)
else:
    exit(self)
