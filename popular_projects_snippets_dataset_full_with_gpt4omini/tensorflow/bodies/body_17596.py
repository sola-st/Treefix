# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
test_func = def_function.function(self._grad(test_func), jit_compile=True)
# The hlo_proto contains statically allocated memory info of HLO values.
hlo_proto_serialized = test_func.experimental_get_compiler_ir(a)(
    stage="optimized_hlo_proto_serialized", device_name=device_name)

hlo_proto = hlo_pb2.HloProto.FromString(hlo_proto_serialized)
allocations = hlo_proto.buffer_assignment.buffer_allocations
exit(sum(getattr(allocation, "size") for allocation in allocations))
