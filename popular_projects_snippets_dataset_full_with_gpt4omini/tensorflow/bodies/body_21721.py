# Extracted from ./data/repos/tensorflow/tensorflow/python/training/queue_runner_test.py
graph = ops.Graph()
with graph.as_default():
    queue = data_flow_ops.FIFOQueue(10, dtypes.float32, name="queue")
    enqueue_op = control_flow_ops.no_op(name="enqueue")
    close_op = control_flow_ops.no_op(name="close")
    cancel_op = control_flow_ops.no_op(name="cancel")
    qr0 = queue_runner_impl.QueueRunner(
        queue, [enqueue_op],
        close_op,
        cancel_op,
        queue_closed_exception_types=(errors_impl.OutOfRangeError,
                                      errors_impl.CancelledError))
    qr0_proto = queue_runner_impl.QueueRunner.to_proto(qr0)
    qr0_recon = queue_runner_impl.QueueRunner.from_proto(qr0_proto)
    self.assertEqual("queue", qr0_recon.queue.name)
    self.assertEqual(1, len(qr0_recon.enqueue_ops))
    self.assertEqual(enqueue_op, qr0_recon.enqueue_ops[0])
    self.assertEqual(close_op, qr0_recon.close_op)
    self.assertEqual(cancel_op, qr0_recon.cancel_op)
    self.assertEqual(
        (errors_impl.OutOfRangeError, errors_impl.CancelledError),
        qr0_recon.queue_closed_exception_types)

    # Assert we reconstruct an OutOfRangeError for QueueRunners
    # created before QueueRunnerDef had a queue_closed_exception_types field.
    del qr0_proto.queue_closed_exception_types[:]
    qr0_legacy_recon = queue_runner_impl.QueueRunner.from_proto(qr0_proto)
    self.assertEqual("queue", qr0_legacy_recon.queue.name)
    self.assertEqual(1, len(qr0_legacy_recon.enqueue_ops))
    self.assertEqual(enqueue_op, qr0_legacy_recon.enqueue_ops[0])
    self.assertEqual(close_op, qr0_legacy_recon.close_op)
    self.assertEqual(cancel_op, qr0_legacy_recon.cancel_op)
    self.assertEqual((errors_impl.OutOfRangeError,),
                     qr0_legacy_recon.queue_closed_exception_types)
