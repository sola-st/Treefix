# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
time_mock = mock.patch.object(time, 'time', autospec=True).start()
time_mock.side_effect = self._mock_time
sleep_mock = mock.patch.object(time, 'sleep', autospec=True).start()
sleep_mock.side_effect = self._mock_sleep

# Mock timeseries where takes longer than timeout.
health_timeseries = ['UNHEALTHY_MAINTENANCE']*50 + ['TIMEOUT']*50
tpu_map = {
    'projects/test-project/locations/us-central1-c/nodes/tpu_name': {
        'ipAddress': '10.1.2.3',
        'port': '8470',
        'state': 'READY',
        'health': health_timeseries,
    },
}

c = client.Client(
    tpu='tpu_name', service=self.mock_service_client(tpu_map=tpu_map))

# Doesn't throw RuntimeError as TPU becomes HEALTHY before timeout
with self.assertRaisesRegex(
    RuntimeError,
    'Timed out waiting for TPU .* to become healthy'):
    c.wait_for_healthy(timeout_s=80, interval=5)
