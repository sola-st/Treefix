# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
"""Get a list of superclasses with minimal amount of non-TF classes.

  Based on many parameters like python version, OS, protobuf implementation
  or changes in google core libraries the list of superclasses of a class
  can change. We only return the first non-TF class to be robust to non API
  affecting changes. The Method Resolution Order returned by `tf_inspect.getmro`
  is still maintained in the return value.

  Args:
    obj: A python routine for us the create the sanitized arspec of.

  Returns:
    list of strings, string representation of the class names.
  """
return_list = []
for cls in tf_inspect.getmro(obj):
    if cls.__name__ == '_NewClass':
        # Ignore class created by @deprecated_alias decorator.
        continue
    str_repr = _NormalizeType(str(cls))
    return_list.append(str_repr)
    # Class type that has keras in their name should also be monitored. This
    # will cover any class imported from third_party/py/keras.
    if 'tensorflow' not in str_repr and 'keras' not in str_repr:
        break

    # Hack - tensorflow.test.StubOutForTesting may or may not be type <object>
    # depending on the environment. To avoid inconsistency, break after we add
    # StubOutForTesting to the return_list.
    if 'StubOutForTesting' in str_repr:
        break

exit(return_list)
