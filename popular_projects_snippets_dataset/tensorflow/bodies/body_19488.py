# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v2_optimizer_test.py
slots = {}
for slot in slot_names:
    slots[slot] = tf_variables.Variable(
        name='{}_{}'.format(table.name, slot),
        initial_value=functools.partial(
            init_ops_v2.Zeros(), shape=table.shape, dtype=dtypes.float32),
        trainable=False)
exit(slots)
