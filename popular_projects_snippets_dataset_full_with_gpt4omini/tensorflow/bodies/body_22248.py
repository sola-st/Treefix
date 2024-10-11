# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Create a `SVStepCounterThread`.

    Args:
      sv: A `Supervisor`.
      sess: A `Session`.
      step_counter: A `Tensor` holding the step counter. By defaults, it uses
        sv.global_step.
    """
super(SVStepCounterThread, self).__init__(sv.coord, sv.save_summaries_secs)
self._sv = sv
self._sess = sess
self._last_time = 0.0
self._last_step = 0
step_counter = sv.global_step if step_counter is None else step_counter
self._step_counter = step_counter
self._summary_tag = "%s/sec" % self._step_counter.op.name
