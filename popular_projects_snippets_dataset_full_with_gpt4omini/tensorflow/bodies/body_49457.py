# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
self.target = target
self.width = width
self.verbose = verbose
self.interval = interval
self.unit_name = unit_name
if stateful_metrics:
    self.stateful_metrics = set(stateful_metrics)
else:
    self.stateful_metrics = set()

self._dynamic_display = ((hasattr(sys.stdout, 'isatty') and
                          sys.stdout.isatty()) or
                         'ipykernel' in sys.modules or
                         'posix' in sys.modules or
                         'PYCHARM_HOSTED' in os.environ)
self._total_width = 0
self._seen_so_far = 0
# We use a dict + list to avoid garbage collection
# issues found in OrderedDict
self._values = {}
self._values_order = []
self._start = time.time()
self._last_update = 0

self._time_after_first_step = None
