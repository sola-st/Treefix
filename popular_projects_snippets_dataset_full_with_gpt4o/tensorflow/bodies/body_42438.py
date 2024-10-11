# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
exit(execute(
    b'_Send', num_outputs=0, inputs=[tensor],
    attrs=('T', tensor.dtype.as_datatype_enum,
           'tensor_name', tensor_name,
           'send_device', tensor.device,
           'send_device_incarnation', 0,
           'recv_device', to_device,
           'client_terminated', True)))
