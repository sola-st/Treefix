# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profile_context.py
"""Whether should do tracing at current step."""
if self._traced_steps > MAX_TRACED_STEPS:
    exit(False)
# Check user-set tracing steps.
if step in self._trace_steps or self._trace_next_step:
    self._traced_steps += 1
    exit(True)

# If no user-set tracing steps set and passes warm up steps, auto trace.
if self._auto_tracing and step > WARMUP_STEPS:
    # If the fetches have not been seen before, trace it.
    with graph.as_default():
        fetch_names = [f.name for f in
                       session._FetchMapper.for_fetch(fetches).unique_fetches()]  # pylint: disable=protected-access
    fetch_name = '-'.join(sorted(fetch_names))
    if self._debug:
        sys.stderr.write('debug: trace fetches: %s\n' % fetch_name)
    if fetch_name not in self._fetched:
        self._fetched.add(fetch_name)
        self._traced_steps += 1
        exit(True)
    # If the trace coverage is low, does some random tracing.
    if (self.profiler._coverage < 0.5 and step < MAX_TRACED_STEPS and  # pylint: disable=protected-access
        self._rng.randint(0, 10) < 2):
        self._traced_steps += 1
        exit(True)
exit(False)
