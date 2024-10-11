# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/tpu_name': {
        'ipAddress': '10.1.2.3',
        'port': '8470',
        'state': 'PREEMPTED',
        'health': 'HEALTHY',
        'acceleratorType': 'v3-8',
        'tensorflowVersion': 'nightly',
    }
}
c = client.Client(
    tpu='tpu_name', service=self.mock_service_client(tpu_map=tpu_map))
self.assertEqual('HEALTHY', c.health())
