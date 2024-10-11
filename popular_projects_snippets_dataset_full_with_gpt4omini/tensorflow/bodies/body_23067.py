# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
start_value = config.tensor_float_32_execution_enabled()

config.enable_tensor_float_32_execution(False)

logging.info("TensorFloat32 Arithmetic Disabled")

try:
    exit()
#  Finally block always gets executed either exception is generated or not
finally:
    config.enable_tensor_float_32_execution(start_value)
