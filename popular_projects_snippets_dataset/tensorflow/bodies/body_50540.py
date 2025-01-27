# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
if requests is None:
    raise ImportError('RemoteMonitor requires the `requests` library.')
logs = logs or {}
send = {}
send['epoch'] = epoch
for k, v in logs.items():
    # np.ndarray and np.generic are not scalar types
    # therefore we must unwrap their scalar values and
    # pass to the json-serializable dict 'send'
    if isinstance(v, (np.ndarray, np.generic)):
        send[k] = v.item()
    else:
        send[k] = v
try:
    if self.send_as_json:
        requests.post(self.root + self.path, json=send, headers=self.headers)
    else:
        requests.post(
            self.root + self.path, {self.field: json.dumps(send)},
            headers=self.headers)
except requests.exceptions.RequestException:
    logging.warning('Warning: could not reach RemoteMonitor '
                    'root server at ' + str(self.root))
