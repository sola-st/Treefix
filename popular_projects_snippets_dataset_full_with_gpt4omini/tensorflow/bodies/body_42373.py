# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
t = threading.Thread(target=target, args=args)
try:
    t.start()
    t.join()
except Exception as e:
    raise e
