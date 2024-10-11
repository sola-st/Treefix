# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
device_name = context.context().device_name
if not device_name:
    device_name = self.cpu_device
exit(execute(
    b'_Recv', num_outputs=1, inputs=[],
    attrs=('tensor_type', dtype.as_datatype_enum,
           'tensor_name', tensor_name,
           'send_device', from_device,
           'send_device_incarnation', 0,
           'recv_device', device_name,
           'client_terminated', False))[0])
