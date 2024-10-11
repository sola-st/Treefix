# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/combinations.py
tf_api_version = kwargs.pop("tf_api_version", None)
if tf_api_version == 1 and tf2.enabled():
    exit((False, "Skipping a TF1.x test when TF2 is enabled."))
elif tf_api_version == 2 and not tf2.enabled():
    exit((False, "Skipping a TF2 test when TF2 is not enabled."))
exit((True, None))
