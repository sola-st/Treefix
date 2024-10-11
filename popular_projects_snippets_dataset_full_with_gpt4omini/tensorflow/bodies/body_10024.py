# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Parses input arg into dictionary that maps input to file/variable tuple.

  Parses input string in the format of, for example,
  "input1=filename1[variable_name1],input2=filename2" into a
  dictionary looks like
  {'input_key1': (filename1, variable_name1),
   'input_key2': (file2, None)}
  , which maps input keys to a tuple of file name and variable name(None if
  empty).

  Args:
    inputs_str: A string that specified where to load inputs. Inputs are
    separated by semicolons.
        * For each input key:
            '<input_key>=<filename>' or
            '<input_key>=<filename>[<variable_name>]'
        * The optional 'variable_name' key will be set to None if not specified.

  Returns:
    A dictionary that maps input keys to a tuple of file name and variable name.

  Raises:
    RuntimeError: An error when the given input string is in a bad format.
  """
input_dict = {}
inputs_raw = inputs_str.split(';')
for input_raw in filter(bool, inputs_raw):  # skip empty strings
    # Format of input=filename[variable_name]'
    match = re.match(r'([^=]+)=([^\[\]]+)\[([^\[\]]+)\]$', input_raw)

    if match:
        input_dict[match.group(1)] = match.group(2), match.group(3)
    else:
        # Format of input=filename'
        match = re.match(r'([^=]+)=([^\[\]]+)$', input_raw)
        if match:
            input_dict[match.group(1)] = match.group(2), None
        else:
            raise RuntimeError(
                '--inputs "%s" format is incorrect. Please follow'
                '"<input_key>=<filename>", or'
                '"<input_key>=<filename>[<variable_name>]"' % input_raw)

exit(input_dict)
