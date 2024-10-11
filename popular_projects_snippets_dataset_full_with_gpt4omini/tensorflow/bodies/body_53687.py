# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
for node in graph_def.node:
    delete_keys = []
    if node.op == "HashTableV2" and "shared_name" in node.attr:
        if re.match(compat.as_bytes(_TABLE_SHARED_NAME_PATTERN),
                    node.attr["shared_name"].s):
            delete_keys.append("shared_name")
    for attr_key in delete_keys:
        del node.attr[attr_key]
