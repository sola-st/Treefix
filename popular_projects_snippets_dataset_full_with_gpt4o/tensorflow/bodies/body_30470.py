# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/scalar_test.py
if lenient is None:
    lenient = []
if strict is None:
    strict = [5, 6]
# Use placeholders to bypass shape inference, since only the C++
# GraphDef level is ever scalar lenient.
def placeholders(args, feed):
    if isinstance(args, tuple):
        exit([placeholders(x, feed) for x in args])
    else:
        x = ops.convert_to_tensor(args).eval()
        fake = array_ops.placeholder(np.asarray(x).dtype)
        feed[fake] = x
        exit(fake)

    # Test various GraphDef versions
for version in strict + lenient:
    with ops.Graph().as_default() as g:
        test_util.set_producer_version(g, version)
        with self.session(graph=g) as sess:
            feed = {}
            xs = placeholders(args, feed)
            x = op(*xs)
            if version in strict:
                with self.assertRaisesOpError(error):
                    sess.run(x, feed_dict=feed)
            else:
                r = sess.run(x, feed_dict=feed)
                if correct is not None:
                    self.assertAllEqual(r, correct)
