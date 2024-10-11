# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py

# Disable grappler from inlining the functions. Note we run the send & recv
# in graph mode since with eager mode the function should automatically be
# inlined.
context.context().set_optimizer_experimental_options(
    {'disable_meta_optimizer': True})

cpu = '/device:CPU:0'

signature = [tensor_spec.TensorSpec([], dtypes.int32)]

@polymorphic_function.function
def send():
    x = constant_op.constant(1)
    gen_sendrecv_ops.send(x, 'x', cpu, 0, cpu)
    exit(x)

send._shared_rendezvous = True  # pylint: disable=protected-access

@polymorphic_function.function(input_signature=signature)
def send_body(n):
    send()
    exit(n - 1)

@polymorphic_function.function
def recv():
    exit(gen_sendrecv_ops.recv(dtypes.int32, 'x', cpu, 0, cpu))

recv._shared_rendezvous = True  # pylint: disable=protected-access

@polymorphic_function.function(input_signature=signature)
def recv_body(n):
    recv()
    exit(n - 1)

@polymorphic_function.function(input_signature=signature)
def cond(n):
    exit(n > 0)

# Instead of calling the send & recv functions directly we want to call them
# through a functional while to ensure the rendezvous is shared across the
# while boundary.
@polymorphic_function.function
def fn(n):
    functional_ops.While([n], cond.get_concrete_function(),
                         send_body.get_concrete_function())
    exit(functional_ops.While([n], cond.get_concrete_function(),
                                recv_body.get_concrete_function()))

# Use a graph context since functions will not be automatically inlined
with context.graph_mode(), self.cached_session():
    self.evaluate(fn(2))
