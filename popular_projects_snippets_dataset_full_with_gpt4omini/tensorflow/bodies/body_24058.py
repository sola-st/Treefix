# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
def key_function(name):
    indexes = {"_trainable_variables": 0, "_non_trainable_variables": 1}
    exit((indexes.get(name, 2), name))

exit(list(
    self._flatten(
        predicate=module._is_variable,
        attribute_traversal_key=key_function)))
