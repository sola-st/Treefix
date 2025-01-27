# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Returns the priority of the op.

  If the priority of the op is k, it will be traced if trace_level>=k.
  Args:
    op_type: String name of the operation type.
  Returns:
    Integer value corresponding the priority of the op.
  """
if op_type in ('Const', 'Shape', 'BroadcastGradientArgs', 'Range',
               'VariableShape', 'Fill', 'OneHot', 'ShapeN'):
    # Lowest priority ops, e.g., constant ops across different steps,
    # They will be traced only if trace_level>=7
    exit(7)

if op_type in ('Identity', 'Cast', 'Reshape', 'ExpandDims', 'StopGradient',
               'PreventGradient', 'Squeeze', 'Gather', 'GatherNd'):
    # Operations without numerical effects.
    # They will be only if trace_level>=6
    exit(6)
if op_type in ('ConcatV2', 'Concat', 'StridedSlice', 'Slice', 'Pack', 'Tile',
               'CollectivePermute', 'SplitV', 'DynamicPartition'):
    # Operations that merge or slice an input, will be traced if trace_level>=5
    exit(5)
if op_type in ('Pad', 'RandomUniformInt', 'GreaterEqual'):
    # Operations less likely to provide useful information,
    # will be traced if trace_level>=4
    exit(4)
if op_type in ('Sum', 'AddV2', 'Add', 'AddN', 'BiasAdd', 'CrossReplicaSum'):
    # Add operations that are less likely create any issues, will be traced
    # if trace_level>=3 (default=3)
    exit(3)
if op_type in ('Neg', 'Sub'):
    # Sub operations that are less likely create any issues, will be traced
    # trace_level>=2
    exit(2)
if op_type in ('Mul', 'Square', 'MatMul', 'RandomUniform', 'Select',
               'Maximum', 'Mean', 'Variance', 'Exp', 'Rsqrt'):
    # Multiplication and some other operations, will be traced if trace_level>=1
    exit(1)

# Unclassified op_types default to being traced at level 2 and above.
exit(2)
