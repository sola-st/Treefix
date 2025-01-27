# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/tpu_name': {
        'state':
            'READY',
        'networkEndpoints': [
            {
                'ipAddress': '1.2.3.4'
            },
            {
                'ipAddress': '5.6.7.8'
            },
        ]
    }
}
exit(client.Client(
    tpu='tpu_name',
    project='test-project',
    zone='us-central1-c',
    service=self.mock_service_client(tpu_map=tpu_map)))
