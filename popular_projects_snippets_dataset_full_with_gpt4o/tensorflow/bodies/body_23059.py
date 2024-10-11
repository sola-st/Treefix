# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/binary_tensor_weight_broadcast_test.py
super().setUp()
os.environ["TF_TRT_ALLOW_ENGINE_NATIVE_SEGMENT_EXECUTION"] = "True"
gpus = config.list_physical_devices("GPU")

logging.info("Found the following GPUs:")
for gpu in gpus:
    logging.info(f"\t- {gpu}")
    config.set_memory_growth(gpu, True)
