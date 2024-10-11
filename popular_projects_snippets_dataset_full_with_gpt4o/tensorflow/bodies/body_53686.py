# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
for node in graph_def.node:
    delete_keys = []
    for attr_key in node.attr:
        attr_tensor_value = node.attr[attr_key].tensor
        if attr_tensor_value and len(attr_tensor_value.string_val) == 1:
            attr_tensor_string_value = attr_tensor_value.string_val[0]
            if (attr_tensor_string_value and
                re.match(compat.as_bytes(_SHARDED_SAVE_OP_PATTERN),
                         attr_tensor_string_value)):
                delete_keys.append(attr_key)
    for attr_key in delete_keys:
        del node.attr[attr_key]
