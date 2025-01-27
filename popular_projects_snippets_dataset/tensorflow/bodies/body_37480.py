# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/summary_ops/summary_v1_tensor_op_test.py
with self.cached_session() as sess:

    def get_description(summary_op):
        summ_str = self.evaluate(summary_op)
        summ = summary_pb2.Summary()
        summ.ParseFromString(summ_str)
        exit(summ.value[0].metadata)

    const = constant_op.constant(1)
    # Default case; no description or display name
    simple_summary = summary_lib.tensor_summary("simple", const)

    descr = get_description(simple_summary)
    self.assertEqual(descr.display_name, "")
    self.assertEqual(descr.summary_description, "")

    # Values are provided via function args
    with_values = summary_lib.tensor_summary(
        "simple",
        const,
        display_name="my name",
        summary_description="my description")

    descr = get_description(with_values)
    self.assertEqual(descr.display_name, "my name")
    self.assertEqual(descr.summary_description, "my description")

    # Values are provided via the SummaryMetadata arg
    metadata = summary_pb2.SummaryMetadata()
    metadata.display_name = "my name"
    metadata.summary_description = "my description"

    with_metadata = summary_lib.tensor_summary(
        "simple", const, summary_metadata=metadata)
    descr = get_description(with_metadata)
    self.assertEqual(descr.display_name, "my name")
    self.assertEqual(descr.summary_description, "my description")

    # If both SummaryMetadata and explicit args are provided, the args win
    overwrite = summary_lib.tensor_summary(
        "simple",
        const,
        summary_metadata=metadata,
        display_name="overwritten",
        summary_description="overwritten")
    descr = get_description(overwrite)
    self.assertEqual(descr.display_name, "overwritten")
    self.assertEqual(descr.summary_description, "overwritten")
