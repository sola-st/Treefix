# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/print_selective_registration_header_test.py
default_ops = 'NoOp:NoOp,_Recv:RecvOp,_Send:SendOp'
graphs = [
    text_format.Parse(d, graph_pb2.GraphDef())
    for d in [GRAPH_DEF_TXT, GRAPH_DEF_TXT_2]
]

ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
    'rawproto', self.WriteGraphFiles(graphs), default_ops)
matmul_prefix = 'Batch'

self.assertListEqual(
    [
        ('AccumulateNV2', None),  #
        ('BiasAdd', 'BiasOp<CPUDevice, float>'),  #
        ('Const', 'ConstantOp'),  #
        ('MatMul', matmul_prefix +
         'MatMulOp<CPUDevice, double, double, double, true>'),  #
        ('MatMul', matmul_prefix +
         'MatMulOp<CPUDevice, float, float, float, true>'),  #
        ('Maximum', 'BinaryOp<CPUDevice, functor::maximum<int64_t>>'),  #
        ('NoOp', 'NoOp'),  #
        ('Reshape', 'ReshapeOp'),  #
        ('_Recv', 'RecvOp'),  #
        ('_Send', 'SendOp'),  #
    ],
    ops_and_kernels)

graphs[0].node[0].ClearField('device')
graphs[0].node[2].ClearField('device')
ops_and_kernels = selective_registration_header_lib.get_ops_and_kernels(
    'rawproto', self.WriteGraphFiles(graphs), default_ops)
self.assertListEqual(
    [
        ('AccumulateNV2', None),  #
        ('BiasAdd', 'BiasOp<CPUDevice, float>'),  #
        ('Const', 'ConstantOp'),  #
        ('MatMul', matmul_prefix +
         'MatMulOp<CPUDevice, double, double, double, true>'),  #
        ('MatMul', matmul_prefix +
         'MatMulOp<CPUDevice, float, float, float, true>'),  #
        ('Maximum', 'BinaryOp<CPUDevice, functor::maximum<int64_t>>'),  #
        ('NoOp', 'NoOp'),  #
        ('Reshape', 'ReshapeOp'),  #
        ('_Recv', 'RecvOp'),  #
        ('_Send', 'SendOp'),  #
    ],
    ops_and_kernels)
