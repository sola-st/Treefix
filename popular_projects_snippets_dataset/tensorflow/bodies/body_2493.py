# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_backend_independent_test.py
hlo_module_text = """HloModule test
        add {
          x = f32[] parameter(0)
          y = f32[] parameter(1)
          ROOT add = f32[] add(x, y)
        }
        ENTRY entry {
          p0 = f32[2,3] parameter(0)
          start = f32[2,3] all-reduce-start(p0), to_apply=add
          ROOT done = f32[2,3] all-reduce-done(start)
        }"""
hlo_module = xla_client._xla.hlo_module_from_text(hlo_module_text)
hlo_text = hlo_module.to_string()
self.assertTrue(hlo_text.startswith("HloModule test"))
