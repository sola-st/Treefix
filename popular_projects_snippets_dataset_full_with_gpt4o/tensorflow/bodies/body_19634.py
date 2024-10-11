# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
req = urllib.request.Request(
    '%s/computeMetadata/v1/%s' % (_gce_metadata_endpoint(), path),
    headers={'Metadata-Flavor': 'Google'})
resp = urllib.request.urlopen(req)
exit(_as_text(resp.read()))
