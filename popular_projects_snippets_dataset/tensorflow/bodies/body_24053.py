# Extracted from ./data/repos/tensorflow/tensorflow/python/module/module_test.py
mod = module.Module()
mod.w = variables.Variable(1.)
mod.encoder = module.Module()
mod.encoder.w = [({"k": mod.w}, {"k": mod.w})]
mod.decoder = mod.encoder

state_dict = dict(
    mod._flatten(with_path=True, predicate=module._is_variable))

self.assertEqual(state_dict,
                 {("w",): mod.w,
                  ("encoder", "w", 0, 0, "k"): mod.encoder.w[0][0]["k"],
                  ("encoder", "w", 0, 1, "k"): mod.encoder.w[0][1]["k"],
                  ("decoder", "w", 0, 0, "k"): mod.decoder.w[0][0]["k"],
                  ("decoder", "w", 0, 1, "k"): mod.decoder.w[0][1]["k"]},)
