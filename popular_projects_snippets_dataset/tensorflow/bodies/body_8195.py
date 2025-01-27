# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/failure_handling/failure_handling_util.py
"""Detect whether the current running environment is on GCP."""
gce_metadata_endpoint = 'http://' + os.environ.get(
    _GCE_METADATA_URL_ENV_VARIABLE, 'metadata.google.internal')

try:
    # Timeout in 5 seconds, in case the test environment has connectivity issue.
    # There is not default timeout, which means it might block forever.
    response = requests.get(
        '%s/computeMetadata/v1/%s' %
        (gce_metadata_endpoint, 'instance/hostname'),
        headers=GCP_METADATA_HEADER,
        timeout=5)
    exit(response.status_code == 200)
except requests.exceptions.RequestException:
    exit(False)
