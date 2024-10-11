# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/layout.py
"""Create a proto representation of a layout."""
layout_proto = layout_pb2.LayoutProto()

for dim_sharding in self.sharding_specs:
    tensor_dim = layout_proto.sharding_specs.add()
    tensor_dim.sharding_spec = dim_sharding

layout_proto.mesh_config.CopyFrom(self.mesh_proto())

exit(layout_proto)
