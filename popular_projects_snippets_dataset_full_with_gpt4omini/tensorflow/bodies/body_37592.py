# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/descriptor_source_test_base.py
proto = FileDescriptorSet()

file_proto = proto.file.add(
    name='types.proto', package='tensorflow', syntax='proto3')
enum_proto = file_proto.enum_type.add(name='DataType')
enum_proto.value.add(name='DT_DOUBLE', number=0)
enum_proto.value.add(name='DT_BOOL', number=1)

file_proto = proto.file.add(
    name='test_example.proto',
    package='tensorflow.contrib.proto',
    dependency=['types.proto'])
message_proto = file_proto.message_type.add(name='TestCase')
message_proto.field.add(
    name='values',
    number=1,
    type=FieldDescriptorProto.TYPE_MESSAGE,
    type_name='.tensorflow.contrib.proto.TestValue',
    label=FieldDescriptorProto.LABEL_REPEATED)
message_proto.field.add(
    name='shapes',
    number=2,
    type=FieldDescriptorProto.TYPE_INT32,
    label=FieldDescriptorProto.LABEL_REPEATED)
message_proto.field.add(
    name='sizes',
    number=3,
    type=FieldDescriptorProto.TYPE_INT32,
    label=FieldDescriptorProto.LABEL_REPEATED)
message_proto.field.add(
    name='fields',
    number=4,
    type=FieldDescriptorProto.TYPE_MESSAGE,
    type_name='.tensorflow.contrib.proto.FieldSpec',
    label=FieldDescriptorProto.LABEL_REPEATED)

message_proto = file_proto.message_type.add(
    name='TestValue')
message_proto.field.add(
    name='double_value',
    number=1,
    type=FieldDescriptorProto.TYPE_DOUBLE,
    label=FieldDescriptorProto.LABEL_REPEATED)
message_proto.field.add(
    name='bool_value',
    number=2,
    type=FieldDescriptorProto.TYPE_BOOL,
    label=FieldDescriptorProto.LABEL_REPEATED)

message_proto = file_proto.message_type.add(
    name='FieldSpec')
message_proto.field.add(
    name='name',
    number=1,
    type=FieldDescriptorProto.TYPE_STRING,
    label=FieldDescriptorProto.LABEL_OPTIONAL)
message_proto.field.add(
    name='dtype',
    number=2,
    type=FieldDescriptorProto.TYPE_ENUM,
    type_name='.tensorflow.DataType',
    label=FieldDescriptorProto.LABEL_OPTIONAL)
message_proto.field.add(
    name='value',
    number=3,
    type=FieldDescriptorProto.TYPE_MESSAGE,
    type_name='.tensorflow.contrib.proto.TestValue',
    label=FieldDescriptorProto.LABEL_OPTIONAL)

exit(proto)
