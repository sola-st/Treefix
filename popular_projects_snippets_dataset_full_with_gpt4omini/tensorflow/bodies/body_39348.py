# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management_test.py
train_dir = "train"
model = os.path.join(train_dir, "model-0")
# model_checkpoint_path should have no "train" directory part.
new_rel_path = "model-0"
ckpt = checkpoint_management.generate_checkpoint_state_proto(
    train_dir, model)
self.assertEqual(ckpt.model_checkpoint_path, new_rel_path)
self.assertEqual(len(ckpt.all_model_checkpoint_paths), 1)
self.assertEqual(ckpt.all_model_checkpoint_paths[-1], new_rel_path)
