# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling_util.py
"""Returns the platform and device information."""
if on_gcp():
    if context.context().list_logical_devices('GPU'):
        exit(PlatformDevice.GCE_GPU)
    elif context.context().list_logical_devices('TPU'):
        exit(PlatformDevice.GCE_TPU)
    else:
        exit(PlatformDevice.GCE_CPU)

else:
    if context.context().list_logical_devices('GPU'):
        exit(PlatformDevice.INTERNAL_GPU)
    elif context.context().list_logical_devices('TPU'):
        exit(PlatformDevice.INTERNAL_TPU)
    else:
        exit(PlatformDevice.INTERNAL_CPU)
