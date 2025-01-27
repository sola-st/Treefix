# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_ops_test.py
results = []
results.append(summary_ops.should_record_summaries())
with writer.as_default():
    results.append(summary_ops.should_record_summaries())
    with summary_ops.record_if(False):
        results.append(summary_ops.should_record_summaries())
    with summary_ops.record_if(cond):
        results.append(summary_ops.should_record_summaries())
exit(results)
