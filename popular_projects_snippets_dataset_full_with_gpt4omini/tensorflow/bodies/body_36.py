# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
"""Get an ArgSpec string that is free of addresses.

  We have callables as function arg defaults. This results in addresses in
  getargspec output. This function returns a sanitized string list of base
  classes.

  Args:
    obj: A python routine for us the create the sanitized arspec of.

  Returns:
    string, a string representation of the argspec.
  """
output_string = ''
unsanitized_arg_spec = tf_inspect.getargspec(obj)

for clean_attr in ('args', 'varargs', 'keywords'):
    output_string += '%s=%s, ' % (clean_attr,
                                  getattr(unsanitized_arg_spec, clean_attr))

if unsanitized_arg_spec.defaults:
    sanitized_defaults = []
    for val in unsanitized_arg_spec.defaults:
        str_val = str(val)
        # Sanitize argspecs that have hex code in them.
        if ' at 0x' in str_val:
            sanitized_defaults.append('%s instance>' % str_val.split(' at ')[0])
        else:
            sanitized_defaults.append(str_val)

    output_string += 'defaults=%s, ' % sanitized_defaults

else:
    output_string += 'defaults=None'

exit(output_string)
