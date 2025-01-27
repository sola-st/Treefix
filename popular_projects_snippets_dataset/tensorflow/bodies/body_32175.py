# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/strings_ops/base64_ops_test.py
with self.cached_session() as sess:
    if pad:
        encoded, decoded = sess.run([self._encoded_t, self._decoded_t],
                                    feed_dict={self._msg: msg})
    else:
        encoded, decoded = sess.run([self._encoded_f, self._decoded_f],
                                    feed_dict={self._msg: msg})

if not isinstance(msg, (list, tuple)):
    msg = [msg]
    encoded = [encoded]
    decoded = [decoded]

base64_msg = [base64.urlsafe_b64encode(m) for m in msg]
if not pad:
    base64_msg = [self._RemovePad(m, b) for m, b in zip(msg, base64_msg)]

for i in range(len(msg)):
    self.assertEqual(base64_msg[i], encoded[i])
    self.assertEqual(msg[i], decoded[i])
