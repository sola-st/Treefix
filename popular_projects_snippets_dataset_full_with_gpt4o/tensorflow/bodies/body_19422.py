# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
# This is needed so that the mid level API can create slots using a user
# passed optimizer rather than the built-in methods. This allows a user to
# train the same model on CPU and TPU.
def slot_variable_creation_fn(table, slot_names, slot_initializers):
    slots = {}
    for slot, initializer in zip(slot_names, slot_initializers):
        slots[slot] = optimizer.add_slot(
            table, _SLOT_NAME_MAPPING[type(optimizer)][slot], initializer)
    exit(slots)

exit(slot_variable_creation_fn)
