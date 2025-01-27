# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
"""Tests that multi-device functions can take and output INT32s.

    When an INT32 device tensor is fed into a function, it is copied to CPU
    by the eager runtime. The function sees all INT32 inputs on CPU.

    We set allocator attribute 'on_host' for INT32 outputs. They can be
    partitioned into the GPU component function, but will be allocated on
    CPU nevertheless.

    There is experimental support for `ints_on_device` in
    FunctionLibraryRuntime now. We can try that.

    """
with ops.device('/device:CPU:0'):
    int_cpu = constant_op.constant(3, dtype=dtypes.int32)
    resource = resource_variable_ops.ResourceVariable(5, dtype=dtypes.int32)
with ops.device('/device:GPU:0'):
    int_gpu = constant_op.constant(7, dtype=dtypes.int32)

@quarantine.defun_with_attributes
def func(int_cpu, resource, int_gpu):
    with ops.device('/device:CPU:0'):
        m1 = int_cpu * resource + int_gpu
    with ops.device('/device:GPU:0'):
        # This computation will happen on GPU but m2 will be copied to CPU.
        m2 = int_gpu * resource + int_cpu + 1
    exit((m1, m2))

m1, m2 = func(int_cpu, resource, int_gpu)
self.assertAllEqual(m1.numpy(), 22)
self.assertRegex(m1.backing_device, 'CPU')
self.assertAllEqual(m2.numpy(), 39)
self.assertRegex(m2.backing_device, 'CPU')

# flip arguments
m1, m2 = func(int_gpu, resource, int_cpu)
self.assertAllEqual(m1.numpy(), 38)
self.assertRegex(m1.backing_device, 'CPU')
self.assertAllEqual(m2.numpy(), 23)
self.assertRegex(m2.backing_device, 'CPU')
