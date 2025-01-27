# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_model_parallelism_test.py
original_device_placement = config.get_soft_device_placement()
config.set_soft_device_placement(True)

strategy, _ = get_tpu_strategy(enable_spmd=True)
summary_dir = self.get_temp_dir()
writer = summary_ops.create_file_writer_v2(summary_dir)
const_multiple = 2
num_iters = 10
expected_event_count = num_iters + 1

with strategy.scope():
    step = variables.Variable(1, dtype=dtypes.int64)

@def_function.function
def run():
    with writer.as_default():
        with summary_ops.record_if(True):
            summary_ops.scalar("result", step * const_multiple, step=step)
            step.assign_add(1)

for _ in range(num_iters):
    strategy.run(run, args=())

for val in step.values:
    for var in val.variables:
        self.assertAllEqual(expected_event_count, var)

events = summary_test_util.events_from_logdir(summary_dir)
self.assertLen(events, expected_event_count)

# Event[0] is generic metadata and summary_ops data starts at event[1].
for logged_step in range(1, expected_event_count):
    self.assertEqual(events[logged_step].summary.value[0].simple_value,
                     logged_step * const_multiple)

config.set_soft_device_placement(original_device_placement)
