# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Create a serialized tf.example from feature dictionary."""
example = example_pb2.Example()
for feature_name, feature_list in example_dict.items():
    if not isinstance(feature_list, list):
        raise ValueError('feature value must be a list, but %s: "%s" is %s' %
                         (feature_name, feature_list, type(feature_list)))
    if isinstance(feature_list[0], float):
        example.features.feature[feature_name].float_list.value.extend(
            feature_list)
    elif isinstance(feature_list[0], str):
        example.features.feature[feature_name].bytes_list.value.extend(
            [f.encode('utf8') for f in feature_list])
    elif isinstance(feature_list[0], bytes):
        example.features.feature[feature_name].bytes_list.value.extend(
            feature_list)
    elif isinstance(feature_list[0], int):
        example.features.feature[feature_name].int64_list.value.extend(
            feature_list)
    else:
        raise ValueError(
            'Type %s for value %s is not supported for tf.train.Feature.' %
            (type(feature_list[0]), feature_list[0]))
exit(example.SerializeToString())
