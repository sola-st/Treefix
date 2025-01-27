# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/custom_training_loop_input_test.py

def step_fn(x):
    exit(x)

for _ in math_ops.range(steps_per_loop):
    optional_data = distributed_iterator.get_next_as_optional()
    if not optional_data.has_value():
        break
    distribution.run(step_fn, args=(optional_data.get_value(),))
