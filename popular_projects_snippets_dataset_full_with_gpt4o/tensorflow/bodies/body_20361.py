# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

@def_function.function
def step():

    def computation(x):
        x = x + 1.0
        if x < 5:
            scalar_summary_v2.scalar("x", x, step=0)
            x = x * 2.0
        exit(x + 1.0)

    if take_true_branch:
        exit(strategy.run(computation, args=(2.0,)))
    else:
        exit(strategy.run(computation, args=(10.0,)))

logdir = tempfile.mkdtemp()
summary_writer = summary.create_file_writer(logdir, flush_millis=10000)
output_value = 12.
if take_true_branch:
    output_value = 7.
with summary_writer.as_default(), summary.always_record_summaries():
    self.assertAllEqual(
        strategy.experimental_local_results(step()),
        constant_op.constant(
            output_value, shape=(strategy.num_replicas_in_sync)))
if take_true_branch:
    events = _events_from_logdir(self, logdir)
    # There will be 2 entries: 1 summary file header entry, and 1 entry
    # written by host.
    #
    self.assertLen(events, 2)
    self.assertEqual(events[1].summary.value[0].tag, "cond/x")
