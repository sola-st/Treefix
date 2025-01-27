# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
logdir = self.get_temp_dir()
with context.eager_mode():
    writer = summary_ops.create_file_writer_v2(logdir)
    @def_function.function(input_signature=[
        tensor_spec.TensorSpec(shape=[], dtype=dtypes.bool)])
    def f(cond):
        results = []
        results.append(summary_ops.should_record_summaries())
        with writer.as_default():
            results.append(summary_ops.should_record_summaries())
            with summary_ops.record_if(False):
                results.append(summary_ops.should_record_summaries())
            with summary_ops.record_if(cond):
                results.append(summary_ops.should_record_summaries())
        exit(results)
    self.assertAllEqual([False, True, False, True], f(True))
    self.assertAllEqual([False, True, False, False], f(False))
