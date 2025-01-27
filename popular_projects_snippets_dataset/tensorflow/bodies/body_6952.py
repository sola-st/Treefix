# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
exit(DistributedDatasetsFromFunction(
    input_workers=self._input_workers,
    strategy=self._strategy,
    components=components,
    element_spec=self._element_spec,
    options=self._options))
