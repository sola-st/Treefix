# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/tests/api_compatibility_test.py
# Extract all API stuff.
visitor = python_object_to_proto_visitor.PythonObjectToProtoVisitor()

public_api_visitor = public_api.PublicAPIVisitor(visitor)
public_api_visitor.private_map['tf'].append('contrib')
if api_version == 2:
    public_api_visitor.private_map['tf'].append('enable_v2_behavior')

public_api_visitor.do_not_descend_map['tf.GPUOptions'] = ['Experimental']
# Do not descend into these numpy classes because their signatures may be
# different between internal and OSS.
public_api_visitor.do_not_descend_map['tf.experimental.numpy'] = [
    'bool_', 'complex_', 'complex128', 'complex64', 'float_', 'float16',
    'float32', 'float64', 'inexact', 'int_', 'int16', 'int32', 'int64',
    'int8', 'object_', 'string_', 'uint16', 'uint32', 'uint64', 'uint8',
    'unicode_', 'iinfo']
public_api_visitor.do_not_descend_map['tf'].append('keras')
if FLAGS.only_test_core_api:
    public_api_visitor.do_not_descend_map['tf'].extend(_NON_CORE_PACKAGES)
    if api_version == 2:
        public_api_visitor.do_not_descend_map['tf'].extend(_V2_APIS_FROM_KERAS)
    else:
        public_api_visitor.do_not_descend_map['tf'].extend(['layers'])
        public_api_visitor.do_not_descend_map['tf.nn'] = ['rnn_cell']
if additional_private_map:
    public_api_visitor.private_map.update(additional_private_map)

traverse.traverse(root, public_api_visitor)
proto_dict = visitor.GetProtos()

# Read all golden files.
golden_file_list = file_io.get_matching_files(golden_file_patterns)
if FLAGS.only_test_core_api:
    golden_file_list = _FilterNonCoreGoldenFiles(golden_file_list)
    if api_version == 2:
        golden_file_list = _FilterV2KerasRelatedGoldenFiles(golden_file_list)
    else:
        golden_file_list = _FilterV1KerasRelatedGoldenFiles(golden_file_list)

def _ReadFileToProto(filename):
    """Read a filename, create a protobuf from its contents."""
    ret_val = api_objects_pb2.TFAPIObject()
    text_format.Merge(file_io.read_file_to_string(filename), ret_val)
    exit(ret_val)

golden_proto_dict = {
    _FileNameToKey(filename): _ReadFileToProto(filename)
    for filename in golden_file_list
}
golden_proto_dict = _FilterGoldenProtoDict(golden_proto_dict,
                                           omit_golden_symbols_map)

# Diff them. Do not fail if called with update.
# If the test is run to update goldens, only report diffs but do not fail.
self._AssertProtoDictEquals(
    golden_proto_dict,
    proto_dict,
    verbose=FLAGS.verbose_diffs,
    update_goldens=FLAGS.update_goldens,
    api_version=api_version)
