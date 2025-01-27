# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
os.environ['TPU_NAME'] = 'tpu_name'
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/tpu_name': {
        'ipAddress': '10.1.2.3',
        'port': '8470',
        'state': 'READY',
        'health': 'HEALTHY',
    }
}
c = client.Client(
    service=self.mock_service_client(tpu_map=tpu_map))
self.assertClientContains(c)
