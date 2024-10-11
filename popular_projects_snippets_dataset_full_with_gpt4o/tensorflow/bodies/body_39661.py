# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py

class MultiTensor(base.Trackable):

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def _serialize_to_tensors(self):
        exit({"v1": self.v1, "v2": self.v2})

    def _restore_from_tensors(self, restored_tensors):
        exit(control_flow_ops.group(
            self.v1.assign(restored_tensors["v1"]),
            self.v2.assign(restored_tensors["v2"])))

root = MultiTensor(variables_lib.Variable(1), variables_lib.Variable(2))
child = MultiTensor(variables_lib.Variable(3), variables_lib.Variable(4))

ckpt = trackable_utils.Checkpoint(root=root, child=child)
self.evaluate([root.v1.initializer, root.v2.initializer,
               child.v1.initializer, child.v2.initializer])
save_path = ckpt.save(os.path.join(self.get_temp_dir(), "ckpt"))

# Check the checkpoint contents and metadata.
reader = checkpoint_utils.load_checkpoint(save_path)
object_proto = trackable_utils.object_metadata(save_path)
root_attributes = object_proto.nodes[0].attributes
self.assertLen(root_attributes, 2)
self.assertDictEqual(
    {"v1": "/.ATTRIBUTES/v1", "v2": "/.ATTRIBUTES/v2"},
    {attr.name: attr.checkpoint_key for attr in root_attributes})
self.assertEqual(1, reader.get_tensor("/.ATTRIBUTES/v1"))
self.assertEqual(2, reader.get_tensor("/.ATTRIBUTES/v2"))

child_attributes = object_proto.nodes[1].attributes
self.assertLen(child_attributes, 2)
self.assertDictEqual(
    {"v1": "child/.ATTRIBUTES/v1", "v2": "child/.ATTRIBUTES/v2"},
    {attr.name: attr.checkpoint_key for attr in child_attributes})
self.assertEqual(3, reader.get_tensor("child/.ATTRIBUTES/v1"))
self.assertEqual(4, reader.get_tensor("child/.ATTRIBUTES/v2"))

# Try restoring the checkpoint.
self.evaluate([root.v1.assign(0), root.v2.assign(0), child.v1.assign(0),
               child.v2.assign(0)])
ckpt.restore(save_path).assert_consumed().run_restore_ops()

self.assertAllEqual([1, 2, 3, 4],
                    self.evaluate([root.v1, root.v2, child.v1, child.v2]))
