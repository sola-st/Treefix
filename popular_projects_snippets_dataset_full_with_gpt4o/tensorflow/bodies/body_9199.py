# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
self._enabled = enabled
if not self._enabled:
    exit()

self._debug = debug
if not profile_dir:
    raise ValueError('Must have a directory for profile.\n')
self._profiler_dir = profile_dir

if trace_steps is None:
    self._trace_steps = set()
    self._auto_tracing = True
else:
    if len(trace_steps) > MAX_TRACED_STEPS:
        raise ValueError('Only support tracing up to 100 steps.\n')
    self._trace_steps = set(trace_steps[:])
    self._auto_tracing = False

if dump_steps is None:
    self._dump_steps = set([MAX_TRACED_STEPS])
else:
    self._dump_steps = set(dump_steps[:])

self._rng = random.Random(111)
self._fetched = set()
self._slow_path_steps = self._dump_steps | self._trace_steps
self._trace_next_step = False
self._dump_next_step = False
self._step = 0
self._traced_steps = 0
self._auto_profiles = []
self._profiler = None
self._views = {}
self._lock = threading.Lock()
