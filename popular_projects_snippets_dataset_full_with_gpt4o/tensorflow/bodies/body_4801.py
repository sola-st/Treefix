# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/test_util.py
"""All-in-one main function for tf.distribute tests."""
if config_logical_devices:
    app.call_after_init(_set_logical_devices)
if enable_v2_behavior:
    v2_compat.enable_v2_behavior()
else:
    v2_compat.disable_v2_behavior()
multi_process_runner.test_main()
