# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
time_mock = mock.patch.object(time, 'time', autospec=True).start()
time_mock.side_effect = self._mock_time
sleep_mock = mock.patch.object(time, 'sleep', autospec=True).start()
sleep_mock.side_effect = self._mock_sleep

health_timeseries = (['UNHEALTHY_MAINTENANCE']*30 + ['TIMEOUT']*10
                     + [None]*20 + ['HEALTHY']*30)
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
timeout = 80
interval = 5
return_time = 60
c.wait_for_healthy(timeout_s=timeout, interval=interval)
self.assertEqual(time.time(), return_time)
self.assertEqual(sleep_mock.call_count, return_time/interval)
