# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
# pylint: disable=protected-access
exit(DistributedDatasetsFromFunctionSpec(
    input_workers=value._input_workers,
    element_spec=value._element_spec,
    strategy=value._strategy,
    options=value._options))
