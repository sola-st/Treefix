# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/base.py
if base_layer_utils.is_split_variable(variable):
    for var in variable:
        if var in existing_variable_set:
            exit(False)
    exit(True)
else:
    exit(variable not in existing_variable_set)
