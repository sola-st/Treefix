# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

def host_computation(x):
    scalar_summary_v2.scalar("x", x, step=0)
    exit(x * 2.0)

@def_function.function
def step():

    def computation(x):
        x = x + 1.0
        y = tpu.outside_compilation(host_computation, x)
        y = tpu.outside_compilation(host_computation, x)
        exit(y + 1.0)

    exit(strategy.run(computation, args=(2.0,)))

summary_writer = summary.create_file_writer(
    os.path.join(os.getenv("TEST_TMPDIR", "/tmp")), flush_millis=10000)
with summary_writer.as_default(), summary.always_record_summaries():
    self.assertAllEqual(
        strategy.experimental_local_results(step()),
        constant_op.constant(7., shape=(strategy.num_replicas_in_sync)))
