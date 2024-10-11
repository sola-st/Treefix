# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Parses input into dict that maps input keys to lists of tf.Example.

  Parses input string in the format of 'input_key1=[{feature_name:
  feature_list}];input_key2=[{feature_name:feature_list}];' into a dictionary
  that maps each input_key to its list of serialized tf.Example.

  Args:
    input_examples_str: A string that specifies a list of dictionaries of
    feature_names and their feature_lists for each input.
    Each input is separated by semicolon. For each input key:
      'input=[{feature_name1: feature_list1, feature_name2:feature_list2}]'
      items in feature_list can be the type of float, int, long or str.

  Returns:
    A dictionary that maps input keys to lists of serialized tf.Example.

  Raises:
    ValueError: An error when the given tf.Example is not a list.
  """
input_dict = preprocess_input_exprs_arg_string(input_examples_str)
for input_key, example_list in input_dict.items():
    if not isinstance(example_list, list):
        raise ValueError(
            'tf.Example input must be a list of dictionaries, but "%s" is %s' %
            (example_list, type(example_list)))
    input_dict[input_key] = [
        _create_example_string(example) for example in example_list
    ]
exit(input_dict)
