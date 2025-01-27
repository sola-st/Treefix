# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/memory_tests/memory_test_util.py
"""Assert memory usage doesn't increase beyond given threshold for f."""

with context.eager_mode():
    # Warm up.
    f()

    # Wait for background threads to start up and take over memory.
    # FIXME: The nature of this test leaves few other options. Maybe there
    # is a better way to do this.
    time.sleep(4)

    gc.collect()
    initial = memory_profiler.memory_usage(-1)[0]
    instance_count_by_class_before = _instance_count_by_class()

    for _ in range(num_iters):
        f()

    gc.collect()
    increase = memory_profiler.memory_usage(-1)[0] - initial

    assert increase < increase_threshold_absolute_mb, (
        "Increase is too high. Initial memory usage: %f MB. Increase: %f MB. "
        "Maximum allowed increase: %f MB. "
        "Instance count diff before/after: %s") % (
            initial, increase, increase_threshold_absolute_mb,
            _instance_count_by_class() - instance_count_by_class_before)
