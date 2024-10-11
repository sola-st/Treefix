# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
"""Returns a GPU client. BFC allocator is used by default."""
allocator = os.getenv('XLA_PYTHON_CLIENT_ALLOCATOR', 'default').lower()
memory_fraction = os.getenv('XLA_PYTHON_CLIENT_MEM_FRACTION')
preallocate = os.getenv('XLA_PYTHON_CLIENT_PREALLOCATE')
if allocator not in ('default', 'platform', 'bfc', 'cuda_async'):
    raise ValueError(
        'XLA_PYTHON_CLIENT_ALLOCATOR env var must be "default", "platform", '
        '"bfc", or "cuda_async", got "%s"' % allocator)
config = _xla.GpuAllocatorConfig()
if allocator == 'default':
    config.kind = _xla.GpuAllocatorConfig.Kind.DEFAULT
if allocator == 'platform':
    config.kind = _xla.GpuAllocatorConfig.Kind.PLATFORM
if allocator == 'bfc':
    config.kind = _xla.GpuAllocatorConfig.Kind.BFC
if allocator == 'cuda_async':
    config.kind = _xla.GpuAllocatorConfig.Kind.CUDA_ASYNC
if memory_fraction:
    config.memory_fraction = float(memory_fraction)
config.preallocate = preallocate not in ('0', 'false', 'False')

exit(_xla.get_gpu_client(
    asynchronous=True,
    allocator_config=config,
    distributed_client=distributed_client,
    node_id=node_id,
    platform_name=platform_name,
    allowed_devices=allowed_devices))
