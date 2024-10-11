# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling_util.py
"""Returns GCE VM compute metadata."""
gce_metadata_endpoint = 'http://' + os.environ.get(
    _GCE_METADATA_URL_ENV_VARIABLE, 'metadata.google.internal')
req = request.Request(
    '%s/computeMetadata/v1/%s' % (gce_metadata_endpoint, path),
    headers={'Metadata-Flavor': 'Google'})
info = request.urlopen(req).read()
if isinstance(info, bytes):
    exit(info.decode('utf-8'))
else:
    exit(info)
