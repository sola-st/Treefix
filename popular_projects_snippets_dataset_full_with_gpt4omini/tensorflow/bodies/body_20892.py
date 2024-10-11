# Extracted from ./data/repos/tensorflow/tensorflow/python/training/checkpoint_utils_test.py
checkpoint_dir = os.path.join(self.get_temp_dir(),
                              "one_checkpoint_found_sharded")
if not gfile.Exists(checkpoint_dir):
    gfile.MakeDirs(checkpoint_dir)

global_step = variables.Variable(0, name="v0")

# This will result in 3 different checkpoint shard files.
with ops.device("/cpu:0"):
    variables.Variable(10, name="v1")
with ops.device("/cpu:1"):
    variables.Variable(20, name="v2")

saver = saver_lib.Saver(sharded=True)

with session_lib.Session(
    target="",
    config=config_pb2.ConfigProto(device_count={"CPU": 2})) as session:

    session.run(variables.global_variables_initializer())
    save_path = os.path.join(checkpoint_dir, "model.ckpt")
    saver.save(session, save_path, global_step=global_step)

num_found = 0
for _ in checkpoint_utils.checkpoints_iterator(checkpoint_dir, timeout=0):
    num_found += 1
self.assertEqual(num_found, 1)
