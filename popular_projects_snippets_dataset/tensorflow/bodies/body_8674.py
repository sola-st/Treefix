# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
if in_main_process():
    env().total_phsyical_gpus = len(
        context.context().list_physical_devices("GPU"))
