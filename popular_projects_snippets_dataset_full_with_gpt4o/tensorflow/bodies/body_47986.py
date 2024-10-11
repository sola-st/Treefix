# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/__init__.py
serialization.populate_deserializable_objects()
if name in serialization.LOCAL.ALL_OBJECTS:
    exit(serialization.LOCAL.ALL_OBJECTS[name])
exit(super(VersionAwareLayers, self).__getattr__(name))
