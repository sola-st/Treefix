# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Remove tensors from model."""
if not remove_tensors_idxs:
    exit()
if len(model.subgraphs) > 1:
    logging.info("Skipping the removal of dangled tensors since the model has "
                 "multiple subgraphs and tensors can be used in the different "
                 "subgraph(s)")
    exit()
subgraph = model.subgraphs[0]
tensors = subgraph.tensors
operators = subgraph.operators

logging.debug("Removing tensors at indices : %s", remove_tensors_idxs)
# An optimized check to validate if "remove_tensors_idxs" (eg: [4,5,6]) is an
# exact subset, with ordering, of "tensors" indices (eg: [0,1,2,3,4,5,6]).
if min(remove_tensors_idxs) == len(tensors) - len(remove_tensors_idxs):
    logging.debug("Removing tensors only at the end of the tensor list")
    del tensors[min(remove_tensors_idxs):]
else:
    logging.debug("Removing tensors requires updating the model")
    # Map the old tensor indices to new tensor indices
    d_old_to_new_tensors = {}
    left_shift_by = 0
    for idx in range(len(tensors)):
        if idx in remove_tensors_idxs:
            left_shift_by += 1
        else:
            d_old_to_new_tensors[idx] = idx - left_shift_by
    logging.debug("Old to new tensors map: %s", d_old_to_new_tensors.__str__())
    # Update tensor indices referenced throughout the model
    def update_tensors(tensor_idxs):
        for i, ti in enumerate(tensor_idxs):
            tensor_idxs[i] = d_old_to_new_tensors.get(ti, -1)
    update_tensors(subgraph.inputs)
    update_tensors(subgraph.outputs)
    for op in operators:
        update_tensors(op.inputs)
        update_tensors(op.outputs)
    if model.signatureDefs:
        signature_def = model.signatureDefs[0]
        _update_signature_def_tensors(signature_def.inputs, d_old_to_new_tensors)
        _update_signature_def_tensors(signature_def.outputs, d_old_to_new_tensors)
    # Delete the tensors
    for idx in sorted(remove_tensors_idxs, reverse=True):
        tensors.pop(idx)
    logging.debug("Removed tensors marked for deletion")
