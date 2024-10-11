# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Constructs a new Timeline.

    A 'Timeline' is used for visualizing the execution of a TensorFlow
    computation.  It shows the timings and concurrency of execution at
    the granularity of TensorFlow Ops.
    This class is not thread safe.

    Args:
      step_stats: The 'StepStats' proto recording execution times.
      graph: (Optional) The 'Graph' that was executed.
    """

self._origin_step_stats = step_stats
self._step_stats = None
self._graph = graph
self._chrome_trace = _ChromeTraceFormatter()
self._next_pid = 0
self._device_pids = {}  # device name -> pid for compute activity.
self._tensor_pids = {}  # device name -> pid for tensors.
self._tensors = {}  # tensor_name -> TensorTracker
self._next_flow_id = 0
self._flow_starts = {}  # tensor_name -> (timestamp, pid, tid)
self._alloc_times = {}  # tensor_name -> ( time, allocator, size )
self._allocator_maximums = {}  # allocator name => maximum bytes long
