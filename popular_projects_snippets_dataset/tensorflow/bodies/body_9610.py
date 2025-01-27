# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
config_pb = config_pb2.ConfigProto()
pool = config_pb.session_inter_op_thread_pool.add()
with session.Session(config=config_pb) as s:
    inp = constant_op.constant(10.0, name='W1')
    results = s.run([inp])
    self.assertAllEqual([10.0], results)

pool = config_pb.session_inter_op_thread_pool.add()
pool.num_threads = 1
with session.Session(config=config_pb) as s:
    inp = constant_op.constant(20.0, name='W2')
    results = s.run([inp])
    self.assertAllEqual([20.0], results)

pool = config_pb.session_inter_op_thread_pool.add()
pool.num_threads = 1
pool.global_name = 't1'
run_options = config_pb2.RunOptions()
run_options.inter_op_thread_pool = (
    len(config_pb.session_inter_op_thread_pool) - 1)
with session.Session(config=config_pb) as s:
    inp = constant_op.constant(30.0, name='W2')
    results = s.run([inp], options=run_options)
    self.assertAllEqual([30.0], results)
