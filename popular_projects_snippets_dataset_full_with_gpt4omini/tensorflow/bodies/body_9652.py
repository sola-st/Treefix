# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
while not stop.is_set():
    time.sleep(random.random() * 0.1)
    self.assertEqual(sess.run(c), 5.0)
