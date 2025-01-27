# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
if function in object_map:
    exit(object_map[function](*args))
# Registered saver/restore functions do not appear in `object_map`, because
# they are not in the object graph.
exit(saved_model_exported_concrete.ExportedConcreteFunction(
    function, tensor_map)(*args))
