# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
flattened_items = []
for item in input_or_output_dict.values():
    flattened_items.extend(item.flatten())
exit(flattened_items)
