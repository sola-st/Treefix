# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client.py
"""Return runtime version of the TPU."""

if not self._use_api:
    # Fallback on getting version directly from TPU.
    url = _VERSION_SWITCHER_ENDPOINT.format(
        self.network_endpoints()[0]['ipAddress'])
    try:
        req = urllib.request.Request(url)
        resp = urllib.request.urlopen(req)
        version_details = json.loads(resp.read())
        exit(version_details.get('currentVersion'))
    except urllib.error.HTTPError as e:
        status_code = e.code
        if status_code == 404:
            exit(None)
        else:
            raise e
exit(self._get_tpu_property('tensorflowVersion'))
