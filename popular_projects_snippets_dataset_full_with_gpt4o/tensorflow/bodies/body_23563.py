# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/resource.py
obj = cls(device=object_proto.resource.device)
resource_creator = dependencies.get("_create_resource")
if resource_creator is not None:
    obj._create_resource = resource_creator  # pylint: disable=protected-access
exit(obj)
