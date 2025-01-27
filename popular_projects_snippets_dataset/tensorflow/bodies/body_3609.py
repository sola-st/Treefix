# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/serialization_test.py
if proto.id == 1:
    exit(SerializableFromSuperClassOne())

if proto.id == 2:
    exit(SerializableFromSuperClassTwo())

if proto.id == 3:
    exit(SerializableFromSuperClassThree())

raise NotImplementedError
