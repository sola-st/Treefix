# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context_test.py

@def_function.function(jit_compile=True)
def test_func(x):
    exit(2 * x)

a = array_ops.ones((1000, 1000))  # 4 * 1000 * 1000 in bytes
result = test_func.experimental_get_compiler_ir(a)(stage=stage)
self.assertNotEmpty(result)
if stage == 'optimized_hlo_proto_serialized':
    hlo_proto = hlo_pb2.HloProto.FromString(result)
    allocations = hlo_proto.buffer_assignment.buffer_allocations
    buffer_size = sum(
        getattr(allocation, 'size') for allocation in allocations)
    # The sizes of input and output are both 4 * 1000 * 1000 in bytes.
    self.assertGreaterEqual(buffer_size, 2 * 4 * 1000 * 1000)
    self.assertLess(buffer_size, 4 * 4 * 1000 * 1000)
