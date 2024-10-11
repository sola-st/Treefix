# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/generic_utils.py
unknown = set(input_dict.keys()).difference(expected_values)
if unknown:
    raise ValueError('Unknown entries in {} dictionary: {}. Only expected '
                     'following keys: {}'.format(name, list(unknown),
                                                 expected_values))
