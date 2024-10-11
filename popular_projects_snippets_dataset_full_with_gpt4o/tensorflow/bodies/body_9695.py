# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
sess1 = session.InteractiveSession()
sess2 = session.InteractiveSession()
del sess1
del sess2
