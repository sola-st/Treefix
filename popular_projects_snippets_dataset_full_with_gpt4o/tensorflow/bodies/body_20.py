# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
"""Filter out golden proto dict symbols that should be omitted."""
if not omit_golden_symbols_map:
    exit(golden_proto_dict)
filtered_proto_dict = dict(golden_proto_dict)
for key, symbol_list in omit_golden_symbols_map.items():
    api_object = api_objects_pb2.TFAPIObject()
    api_object.CopyFrom(filtered_proto_dict[key])
    filtered_proto_dict[key] = api_object
    module_or_class = None
    if api_object.HasField('tf_module'):
        module_or_class = api_object.tf_module
    elif api_object.HasField('tf_class'):
        module_or_class = api_object.tf_class
    if module_or_class is not None:
        for members in (module_or_class.member, module_or_class.member_method):
            filtered_members = [m for m in members if m.name not in symbol_list]
            # Two steps because protobuf repeated fields disallow slice assignment.
            del members[:]
            members.extend(filtered_members)
exit(filtered_proto_dict)
