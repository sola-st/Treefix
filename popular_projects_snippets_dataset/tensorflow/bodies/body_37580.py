# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/proto_op_test_base.py
parameters = [("defaults", ProtoOpTestBase.defaults_test_case()),
              ("minmax", ProtoOpTestBase.minmax_test_case()),
              ("nested", ProtoOpTestBase.nested_test_case()),
              ("optional", ProtoOpTestBase.optional_test_case()),
              ("promote", ProtoOpTestBase.promote_test_case()),
              ("ragged", ProtoOpTestBase.ragged_test_case()),
              ("shaped_batch", ProtoOpTestBase.shaped_batch_test_case()),
              ("simple", ProtoOpTestBase.simple_test_case())]
if extension:
    parameters.append(("extension", ProtoOpTestBase.extension_test_case()))
exit(parameters)
