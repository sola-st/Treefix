# Extracted from ./data/repos/tensorflow/tensorflow/python/client/timeline.py
"""Produce a counter series for each memory allocator."""
# Iterate over all tensor trackers to build a list of allocations and
# frees for each allocator. Then sort the lists and emit a cumulative
# counter series for each allocator.
allocations = {}
for name in self._tensors:
    tensor = self._tensors[name]
    self._chrome_trace.emit_obj_delete('Tensor', name, tensor.last_unref,
                                       tensor.pid, 0, tensor.object_id)
    allocator = tensor.allocator
    if allocator not in allocations:
        allocations[allocator] = []
    num_bytes = tensor.num_bytes
    allocations[allocator].append((tensor.create_time, num_bytes, name))
    allocations[allocator].append((tensor.last_unref, -num_bytes, name))

alloc_maxes = {}

# Generate a counter series showing total allocations for each allocator.
for allocator in allocations:
    alloc_list = allocations[allocator]
    alloc_list.sort()
    total_bytes = 0
    alloc_tensor_set = set()
    alloc_maxes[allocator] = AllocationMaximum(
        timestamp=0, num_bytes=0, tensors=set())
    for time, num_bytes, name in sorted(
        alloc_list, key=lambda allocation: allocation[0]):
        total_bytes += num_bytes
        if num_bytes < 0:
            alloc_tensor_set.discard(name)
        else:
            alloc_tensor_set.add(name)

        if total_bytes > alloc_maxes[allocator].num_bytes:
            alloc_maxes[allocator] = AllocationMaximum(
                timestamp=time,
                num_bytes=total_bytes,
                tensors=copy.deepcopy(alloc_tensor_set))

        self._chrome_trace.emit_counter('Memory', allocator,
                                        self._allocators_pid, time, allocator,
                                        total_bytes)
self._allocator_maximums = alloc_maxes
