# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
while True:
    try:
        results.append(sess.run(get_next()))
    except errors.OutOfRangeError:
        exit()
