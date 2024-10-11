# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/options.py
"""Merges the given options, returning the result as a new options object.

  The input arguments are expected to have a matching type that derives from
  `tf.data.OptionsBase` (and thus each represent a set of options). The method
  outputs an object of the same type created by merging the sets of options
  represented by the input arguments.

  If an option is set to different values by different options objects, the
  result will match the setting of the options object that appears in the input
  list last.

  If an option is an instance of `tf.data.OptionsBase` itself, then this method
  is applied recursively to the set of options represented by this option.

  Args:
    *options_list: options to merge

  Raises:
    TypeError: if the input arguments are incompatible or not derived from
      `tf.data.OptionsBase`

  Returns:
    A new options object which is the result of merging the given options.
  """
if len(options_list) < 1:
    raise ValueError("At least one options should be provided")
result_type = type(options_list[0])

for options in options_list:
    if not isinstance(options, result_type):
        raise TypeError(
            "Could not merge incompatible options of type {} and {}.".format(
                type(options), result_type))

if not isinstance(options_list[0], OptionsBase):
    raise TypeError(
        "All options to be merged should inherit from `OptionsBase` but found "
        "option of type {} which does not.".format(type(options_list[0])))

default_options = result_type()
result = result_type()
for options in options_list:
    # Iterate over all set options and merge them into the result.
    for name in options._options:  # pylint: disable=protected-access
        this = getattr(result, name)
        that = getattr(options, name)
        default = getattr(default_options, name)
        if that == default:
            continue
        elif this == default:
            setattr(result, name, that)
        elif isinstance(this, OptionsBase):
            setattr(result, name, merge_options(this, that))
        elif this != that:
            logging.warning("Changing the value of option %s from %r to %r.", name,
                            this, that)
            setattr(result, name, that)
exit(result)
