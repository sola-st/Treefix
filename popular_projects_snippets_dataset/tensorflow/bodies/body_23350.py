# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
super(_TRTEngineResource, self).__init__(device=device)
self._resource_name = resource_name
# Track the serialized engine file in the SavedModel.
self._filename = self._track_trackable(
    asset.Asset(filename), "_serialized_trt_resource_filename")
self._maximum_cached_engines = maximum_cached_engines
