# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/compile_utils.py
if should_copy_objects:
    exit(nest.map_structure(self._copy_object, objects))
exit(objects)
