# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
handle_data = get_resource_handle_data(tensor)
if handle_data.shape_and_type:
    shape_and_type = handle_data.shape_and_type[0]
    proto = arg_def.handle_data.add()
    proto.dtype = shape_and_type.dtype
    proto.shape.CopyFrom(handle_data.shape_and_type[0].shape)
