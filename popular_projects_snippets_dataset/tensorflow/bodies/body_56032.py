# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/test_combinations.py
if self._parameter_name in requested_parameters:
    exit({})
else:
    exit({self._parameter_name: ParameterModifier.DO_NOT_PASS_TO_THE_TEST})
