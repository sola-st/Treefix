# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/sample_from_datasets_test.py
if weights_type == "list":
    exit(weights_list)
if weights_type == "tensor":
    exit(ops.convert_to_tensor(weights_list, name="weights"))
exit(dataset_ops.Dataset.from_tensors(weights_list).repeat())
