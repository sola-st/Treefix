# Extracted from ./data/repos/tensorflow/tensorflow/core/tfrt/saved_model/tests/gen_data.py
dataset = dataset_ops.Dataset.from_tensors(x)
r = dataset.map(lambda x: x + 1)
exit(r.get_single_element())
