# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
outputs = model.test_step(data)
# Ensure counter is updated only if `test_step` succeeds.
with ops.control_dependencies(_minimum_control_deps(outputs)):
    model._test_counter.assign_add(1)  # pylint: disable=protected-access
exit(outputs)
