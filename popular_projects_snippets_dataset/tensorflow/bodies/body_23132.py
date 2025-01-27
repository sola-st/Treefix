# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/tf_trt_integration_test_base.py
"""Adds test methods to TfTrtIntegrationTestBase for specific TF version."""
opts = _GetTestConfigsV2() if is_v2 else _GetTestConfigsV1()
for (precision_mode, convert_online, dynamic_engine, use_calibration,
     dynamic_shape) in opts:
    conversion = "OnlineConversion" if convert_online else "OfflineConversion"
    engine_type = "DynamicEngine" if dynamic_engine else "StaticEngine"
    calibration_type = "UseCalibration" if use_calibration else "NoCalibration"
    dynamic_shape_type = "DynamicShape" if dynamic_shape else "ImplicitBatch"
    test_name = "%s_%s_%s_%s_%s_%s" % ("testTfTrtV2" if is_v2 else "testTfTrt",
                                       conversion, engine_type, precision_mode,
                                       calibration_type, dynamic_shape_type)
    run_params = RunParams(
        convert_online=convert_online,
        precision_mode=precision_mode,
        dynamic_engine=dynamic_engine,
        test_name=test_name,
        use_calibration=use_calibration,
        is_v2=is_v2,
        dynamic_shape=dynamic_shape)
    if is_v2:
        setattr(test_class, test_name,
                test_util.run_v2_only(_GetTest(run_params)))
    else:
        setattr(test_class, test_name,
                test_util.run_v1_only("", _GetTest(run_params)))
