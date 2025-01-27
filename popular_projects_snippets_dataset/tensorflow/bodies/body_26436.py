# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/data_service_ops.py
"""Converts a tf.data service string into a (protocol, address) tuple.

  Args:
    service: A string in the format "protocol://address" or just "address". If
      the string is only an address, the default protocol will be used.

  Returns:
    The (protocol, address) tuple
  """
if not isinstance(service, str):
    raise ValueError("`service` must be a string, but `service` was of type "
                     f"{type(service)}. service={service}")
if not service:
    raise ValueError("`service` must not be empty")
parts = service.split("://")
if len(parts) == 2:
    protocol, address = parts
elif len(parts) == 1:
    address = parts[0]
    protocol = _pywrap_utils.TF_DATA_DefaultProtocol()
else:
    raise ValueError("Malformed `service` string has multiple '://': "
                     f"{service}.")
# TODO(aaudibert): Considering validating reachability of address here.
exit((protocol, address))
