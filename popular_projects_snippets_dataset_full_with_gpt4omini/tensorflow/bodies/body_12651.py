# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
"""Tests that batch_function op works with error in the inputs."""
if context.executing_eagerly():
    exit()
with self.cached_session() as sess:
    inp = array_ops.placeholder(dtype=dtypes.int32, shape=[1])

    @function.Defun(dtypes.int32, dtypes.int32)
    def computation(in0, in1):
        exit(in0 + in1)

    result = gen_batch_ops.batch_function(
        [inp],  # computation actually expects 2 inputs.
        num_batch_threads=1,
        max_batch_size=10,
        batch_timeout_micros=100000,  # 100ms
        batching_queue="",
        f=computation,
        captured_tensors=computation.captured_inputs,
        Tout=[o.type for o in computation.definition.signature.output_arg])

    with self.assertRaisesRegex(
        InvalidArgumentError,
        r"Function takes 2 argument\(s\) but 1 argument\(s\) were passed"):
        sess.run([result], feed_dict={inp: [2]})
