# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/print_selective_registration_header_test.py
default_ops = ''
# Test with 2 different ops.
ops_list = """[["Add", "BinaryOp<CPUDevice, functor::add<float>>"],
        ["Softplus", "SoftplusOp<CPUDevice, float>"]]"""
ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
    'ops_list', self.WriteTextFile(ops_list), default_ops)
self.assertListEqual([
    ('Add', 'BinaryOp<CPUDevice, functor::add<float>>'),
    ('Softplus', 'SoftplusOp<CPUDevice, float>'),
], ops_and_kernels)

# Test with a single op.
ops_list = '[["Softplus", "SoftplusOp<CPUDevice, float>"]]'
ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
    'ops_list', self.WriteTextFile(ops_list), default_ops)
self.assertListEqual([
    ('Softplus', 'SoftplusOp<CPUDevice, float>'),
], ops_and_kernels)

# Test with duplicated op.
ops_list = """[["Add", "BinaryOp<CPUDevice, functor::add<float>>"],
        ["Add", "BinaryOp<CPUDevice, functor::add<float>>"]]"""
ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
    'ops_list', self.WriteTextFile(ops_list), default_ops)
self.assertListEqual([
    ('Add', 'BinaryOp<CPUDevice, functor::add<float>>'),
], ops_and_kernels)

# Test op with no kernel.
ops_list = '[["Softplus", ""]]'
ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
    'ops_list', self.WriteTextFile(ops_list), default_ops)
self.assertListEqual([
    ('Softplus', None),
], ops_and_kernels)

# Test two ops_list files.
ops_list = '[["Softplus", "SoftplusOp<CPUDevice, float>"]]'
ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
    'ops_list',
    self.WriteTextFile(ops_list) + self.WriteTextFile(ops_list),
    default_ops)
self.assertListEqual([
    ('Softplus', 'SoftplusOp<CPUDevice, float>'),
], ops_and_kernels)

# Test empty file.
ops_list = ''
with self.assertRaises(Exception):
    ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
        'ops_list', self.WriteTextFile(ops_list), default_ops)
