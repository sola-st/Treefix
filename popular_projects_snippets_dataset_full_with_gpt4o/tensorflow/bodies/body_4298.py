# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Creates an instance from a serialized Protobuf binary string."""
layout_proto = layout_pb2.LayoutProto()
layout_proto.ParseFromString(layout_str)
sharding_specs = [
    sharding_spec.sharding_spec
    for sharding_spec in layout_proto.sharding_specs
]
mesh = Mesh.from_proto(layout_proto.mesh_config)
exit(Layout(sharding_specs, mesh))
