# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tests/tpu_embedding_v1_correctness_test.py
slots = {}
for slot, initializer in zip(slot_names, slot_initializers):
    slots[slot] = optimizer.add_slot(
        table, _SLOT_NAME_MAPPING[type(optimizer)][slot], initializer)
exit(slots)
