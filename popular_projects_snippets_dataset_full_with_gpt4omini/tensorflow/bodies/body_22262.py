# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_large_variable_test.py
save_path = os.path.join(self.get_temp_dir(), "large_variable")
with session.Session("", graph=ops.Graph()) as sess:
    # Declare a variable that is exactly 2GB. This should fail,
    # because a serialized checkpoint includes other header
    # metadata.
    with ops.device("/cpu:0"):
        var = variables.Variable(
            constant_op.constant(
                False, shape=[2, 1024, 1024, 1024], dtype=dtypes.bool))
    save = saver.Saver(
        {
            var.op.name: var
        }, write_version=saver_pb2.SaverDef.V1)
    var.initializer.run()
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                "Tensor slice is too large to serialize"):
        save.save(sess, save_path)
