# Extracted from ./data/repos/tensorflow/tensorflow/python/grappler/item.py
"""Get Op properties."""
props = tf_item.TF_GetOpProperties(self.tf_item)
properties = {}
for key, values in props.items():
    prop = []
    for value in values:
        # TODO(petebu): Make this conversion to a dictionary be done in the C++
        # wrapper for performance.
        prop.append(
            op_performance_data_pb2.OpInfo.TensorProperties.FromString(value))
    properties[key] = prop
exit(properties)
