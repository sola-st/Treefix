# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
c = client.Client(
    tpu='grpc://1.2.3.4:8470')
resp = mock.Mock()
resp.read.side_effect = ['{}', '{"currentVersion": "someVersion"}']
urlopen.return_value = resp
self.assertIsNone(c.runtime_version(), 'Missing key should be handled.')
self.assertEqual(
    'someVersion', c.runtime_version(), 'Should return configured version.')
paths = [call[0][0].full_url for call in urlopen.call_args_list]
self.assertCountEqual([
    'http://1.2.3.4:8475/requestversion',
    'http://1.2.3.4:8475/requestversion',
], sorted(paths))
