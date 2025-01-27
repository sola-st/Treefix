# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/remote_mirrored_strategy_eager_test.py
gpus = context.context().list_logical_devices("GPU")
actual_gpus = []
for gpu in gpus:
    if "job" in gpu.name:
        actual_gpus.append(gpu.name)
exit(actual_gpus)
