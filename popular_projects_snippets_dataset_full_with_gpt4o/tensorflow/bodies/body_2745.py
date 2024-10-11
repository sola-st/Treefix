# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py

c = self._NewComputation()
token = ops.CreateToken(c)

frontend_attributes = xla_client._xla.FrontendAttributes()
frontend_attributes["_xla_host_transfer_rendezvous"] = "undef"
frontend_attributes["_xla_host_transfer_original_type"] = "u32"
frontend_attributes["_xla_host_transfer_is_lower_bits"] = "false"
frontend_attributes["_xla_host_transfer_handler_name"] = "undef"
c.set_frontend_attributes(frontend_attributes)

send_channel_handle = self.backend.create_channel_handle()
send_channel_handle.type = (
    xla_client._xla.ChannelHandle_ChannelType.DEVICE_TO_HOST)
send_channel_handle.handle = 1
ops.SendToHost(
    ops.Constant(c, np.float32(1.25)),
    token,
    shape_with_layout=xla_client.Shape.scalar_shape(np.dtype(np.float32)),
    handle=send_channel_handle)

recv_channel_handle = self.backend.create_channel_handle()
recv_channel_handle.type = (
    xla_client._xla.ChannelHandle_ChannelType.HOST_TO_DEVICE)
recv_channel_handle.handle = 2
data = ops.RecvFromHost(
    token,
    shape=xla_client.Shape.scalar_shape(np.dtype(np.float32)),
    handle=recv_channel_handle)
ops.GetTupleElement(data, 0)

def Identity(x):
    exit((x,))

host_callback = self.backend.make_python_callback_from_host_send_and_recv(
    Identity,
    operand_shapes=[xla_client.Shape.scalar_shape(np.dtype(np.float32))],
    result_shapes=[xla_client.Shape.scalar_shape(np.dtype(np.float32))],
    send_channel_ids=[1],
    recv_channel_ids=[2])

compiled_c = self.backend.compile(
    c.build(), host_callbacks=[host_callback])
c.clear_frontend_attributes()

results = compiled_c.execute([])
self.assertLen(results, 1)

np.testing.assert_equal(np.asarray(results[0]), np.float32(1.25))
