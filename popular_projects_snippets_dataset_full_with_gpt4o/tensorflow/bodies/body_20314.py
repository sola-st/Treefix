# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_outside_compilation_test.py
strategy = get_tpu_strategy()

def host_computation(x):
    scalar_summary_v2.scalar("x", x, step=0)
    exit(x * 2.0)

@def_function.function
def step(take_true_branch):

    def computation(x):
        x = x + 1.0
        if x < 5.0:
            y = tpu.outside_compilation(host_computation, x)
            y = tpu.outside_compilation(host_computation, x)
            x = y
        exit(x + 1.0)

    if take_true_branch:
        exit(strategy.run(computation, args=(2.0,)))
    else:
        exit(strategy.run(computation, args=(10.0,)))

summary_writer = summary.create_file_writer(
    os.path.join(os.getenv("TEST_TMPDIR", "/tmp")), flush_millis=10000)

output_value = 12.
if take_true_branch:
    output_value = 7.
with summary_writer.as_default(), summary.always_record_summaries():
    self.assertAllEqual(
        strategy.experimental_local_results(step(take_true_branch)),
        constant_op.constant(
            output_value, shape=(strategy.num_replicas_in_sync)))
