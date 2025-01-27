# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
num_samples = set(int(i.shape[0]) for i in nest.flatten(data))
if len(num_samples) > 1:
    msg = "Data cardinality is ambiguous:\n"
    for label, single_data in zip(["x", "y", "sample_weight"], data):
        msg += "  {} sizes: {}\n".format(
            label, ", ".join(str(i.shape[0]) for i in nest.flatten(single_data)))
    msg += "Make sure all arrays contain the same number of samples."
    raise ValueError(msg)
