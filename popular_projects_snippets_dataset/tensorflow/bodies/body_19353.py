# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Writes the config section of the report."""

self._write_report('%s %s\n'%(_MARKER_SECTION_BEGIN, _SECTION_NAME_CONFIG))
self._write_report('%s %s\n'%(_FIELD_NAME_VERSION, tt_config.version))
self._write_report('%s %s\n'%(_FIELD_NAME_DEVICE, tt_config.device_type))
self._write_report('%s %s\n'%(_FIELD_NAME_TRACE_MODE,
                              tt_parameters.trace_mode))
self._write_report('%s %s\n'%(_FIELD_NAME_SUBMODE,
                              tt_parameters.submode))
self._write_report('%s %s\n'%(_FIELD_NAME_NUM_REPLICAS,
                              tt_config.num_replicas))
self._write_report('%s %s\n'%(_FIELD_NAME_NUM_REPLICAS_PER_HOST,
                              tt_config.num_replicas_per_host))
self._write_report('%s %s\n'%(_FIELD_NAME_NUM_HOSTS, tt_config.num_hosts))
self._write_report('%s %s\n'%(_MARKER_SECTION_END, _SECTION_NAME_CONFIG))
