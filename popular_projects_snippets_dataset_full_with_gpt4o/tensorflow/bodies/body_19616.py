# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
test_cases = [
    ({
        'projects/test-project/locations/us-central1-c/nodes/tpu_name': {
            'state':
                'READY',
            'symptoms': [{
                'createTime': '2000-01-01T00:29:30.123456Z',
                'symptomType': 'OUT_OF_MEMORY',
                'details': 'The TPU runtime has run OOM at timestamp '
                           '2020-05-29T04:51:32.038721+00:00',
                'workerId': '0'
            }]
        }
    }, True),
]

FLAGS.runtime_oom_exit = False
for tpu_map, want in test_cases:
    c = client.Client(tpu='tpu_name',
                      service=self.mock_service_client(tpu_map=tpu_map))
    self.assertEqual(want, c.recoverable())
FLAGS.runtime_oom_exit = True
