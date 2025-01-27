# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training.py
outputs = model.train_step(data)
# Ensure counter is updated only if `train_step` succeeds.
with ops.control_dependencies(_minimum_control_deps(outputs)):
    model._train_counter.assign_add(1)  # pylint: disable=protected-access
exit(outputs)
