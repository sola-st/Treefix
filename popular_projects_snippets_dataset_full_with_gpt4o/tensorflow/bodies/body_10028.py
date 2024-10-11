# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Parses input arg strings and create inputs feed_dict.

  Parses '--inputs' string for inputs to be loaded from file, and parses
  '--input_exprs' string for inputs to be evaluated from python expression.
  '--input_examples' string for inputs to be created from tf.example feature
  dictionary list.

  Args:
    inputs_str: A string that specified where to load inputs. Each input is
        separated by semicolon.
        * For each input key:
            '<input_key>=<filename>' or
            '<input_key>=<filename>[<variable_name>]'
        * The optional 'variable_name' key will be set to None if not specified.
        * File specified by 'filename' will be loaded using numpy.load. Inputs
            can be loaded from only .npy, .npz or pickle files.
        * The "[variable_name]" key is optional depending on the input file type
            as descripted in more details below.
        When loading from a npy file, which always contains a numpy ndarray, the
        content will be directly assigned to the specified input tensor. If a
        variable_name is specified, it will be ignored and a warning will be
        issued.
        When loading from a npz zip file, user can specify which variable within
        the zip file to load for the input tensor inside the square brackets. If
        nothing is specified, this function will check that only one file is
        included in the zip and load it for the specified input tensor.
        When loading from a pickle file, if no variable_name is specified in the
        square brackets, whatever that is inside the pickle file will be passed
        to the specified input tensor, else SavedModel CLI will assume a
        dictionary is stored in the pickle file and the value corresponding to
        the variable_name will be used.
    input_exprs_str: A string that specifies python expressions for inputs.
        * In the format of: '<input_key>=<python expression>'.
        * numpy module is available as np.
    input_examples_str: A string that specifies tf.Example with dictionary.
        * In the format of: '<input_key>=<[{feature:value list}]>'

  Returns:
    A dictionary that maps input tensor keys to numpy ndarrays.

  Raises:
    RuntimeError: An error when a key is specified, but the input file contains
        multiple numpy ndarrays, none of which matches the given key.
    RuntimeError: An error when no key is specified, but the input file contains
        more than one numpy ndarrays.
  """
tensor_key_feed_dict = {}

inputs = preprocess_inputs_arg_string(inputs_str)
input_exprs = preprocess_input_exprs_arg_string(input_exprs_str)
input_examples = preprocess_input_examples_arg_string(input_examples_str)

for input_tensor_key, (filename, variable_name) in inputs.items():
    data = np.load(file_io.FileIO(filename, mode='rb'), allow_pickle=True)  # pylint: disable=unexpected-keyword-arg

    # When a variable_name key is specified for the input file
    if variable_name:
        # if file contains a single ndarray, ignore the input name
        if isinstance(data, np.ndarray):
            logging.warn(
                'Input file %s contains a single ndarray. Name key \"%s\" ignored.'
                % (filename, variable_name))
            tensor_key_feed_dict[input_tensor_key] = data
        else:
            if variable_name in data:
                tensor_key_feed_dict[input_tensor_key] = data[variable_name]
            else:
                raise RuntimeError(
                    'Input file %s does not contain variable with name \"%s\".' %
                    (filename, variable_name))
    # When no key is specified for the input file.
    else:
        # Check if npz file only contains a single numpy ndarray.
        if isinstance(data, np.lib.npyio.NpzFile):
            variable_name_list = data.files
            if len(variable_name_list) != 1:
                raise RuntimeError(
                    'Input file %s contains more than one ndarrays. Please specify '
                    'the name of ndarray to use.' % filename)
            tensor_key_feed_dict[input_tensor_key] = data[variable_name_list[0]]
        else:
            tensor_key_feed_dict[input_tensor_key] = data

  # When input is a python expression:
for input_tensor_key, py_expr_evaluated in input_exprs.items():
    if input_tensor_key in tensor_key_feed_dict:
        logging.warn(
            'input_key %s has been specified with both --inputs and --input_exprs'
            ' options. Value in --input_exprs will be used.' % input_tensor_key)
    tensor_key_feed_dict[input_tensor_key] = py_expr_evaluated

# When input is a tf.Example:
for input_tensor_key, example in input_examples.items():
    if input_tensor_key in tensor_key_feed_dict:
        logging.warn(
            'input_key %s has been specified in multiple options. Value in '
            '--input_examples will be used.' % input_tensor_key)
    tensor_key_feed_dict[input_tensor_key] = example
exit(tensor_key_feed_dict)
