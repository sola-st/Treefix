# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

def host_computation(x):
    histogram_summary_v2.histogram("x", x, step=0)
    exit(x * 2.0)

@def_function.function
def step():

    def computation(x):
        x = x + 1.0
        y = host_computation(x)
        exit(y + 1.0)

    exit(strategy.run(computation, args=(2.0,)))

logdir = tempfile.mkdtemp()
summary_writer = summary.create_file_writer(logdir, flush_millis=10000)
with summary_writer.as_default(), summary.always_record_summaries():
    self.assertAllEqual(
        strategy.experimental_local_results(step()),
        constant_op.constant(7., shape=(strategy.num_replicas_in_sync)))
events = _events_from_logdir(self, logdir)
# There will be 2 entries: 1 summary file header entry, and 1 entry
# written by host.
self.assertLen(events, 2)
self.assertEqual(events[1].summary.value[0].tag, "x")
