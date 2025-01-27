# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_util.py
super().__init__(methodName)
# Make sure we get unfiltered stack traces during the test
traceback_utils.disable_traceback_filtering()
if is_xla_enabled():
    pywrap_tf_session.TF_SetXlaAutoJitMode("2")
    pywrap_tf_session.TF_SetXlaMinClusterSize(1)
    pywrap_tf_session.TF_SetXlaEnableLazyCompilation(False)
    pywrap_tf_session.TF_SetTfXlaCpuGlobalJit(True)
    # Constant folding secretly runs code on TF:Classic CPU, so we also
    # disable it here.
    pywrap_tf_session.TF_SetXlaConstantFoldingDisabled(True)

# Check if the mlir bridge has been explicitly enabled or disabled. If
# is_mlir_bridge_enabled() returns None, the user did not explictly enable
# or disable the bridge so do not update enable_mlir_bridge.
if is_mlir_bridge_enabled():
    context.context().enable_mlir_bridge = True
elif is_mlir_bridge_enabled() is not None:
    context.context().enable_mlir_bridge = False

self._threads = []
self._tempdir = None
self._cached_session = None
self._test_start_time = None
# This flag provides the ability to control whether the graph mode gets
# initialized for TF1 or not. Initializing for TF1, which is what was
# happening earlier, was preventing enablement of 'eager mode' in the test.
self._set_default_seed = True
