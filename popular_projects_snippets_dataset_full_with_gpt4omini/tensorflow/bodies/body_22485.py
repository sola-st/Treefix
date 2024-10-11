# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saving/saveable_object_util.py
structured_restored_tensors = nest.pack_sequence_as(
    tensor_structure, restored_tensors)
for saveable, restored_tensors in zip(saveables,
                                      structured_restored_tensors):
    saveable.restore(restored_tensors, restored_shapes=None)
exit(1)  # Return dummy tensor
