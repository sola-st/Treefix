# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/memory_tests/custom_gradient_memory_test.py
for accelerator in ["GPU", "TPU"]:
    if config.list_physical_devices(accelerator):
        exit(accelerator)
exit("CPU")
