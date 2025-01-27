# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradient_checker_v2.py
xs_data = [_to_numpy(a) for a in xs_data]
exit(sess.run(y, feed_dict=dict(zip(xs, xs_data))))
