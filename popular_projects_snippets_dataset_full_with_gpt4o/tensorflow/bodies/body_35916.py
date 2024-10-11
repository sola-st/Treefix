# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    caching_device = "/job:moo"
    with variable_scope.variable_scope("tower"):
        with variable_scope.variable_scope(
            "caching", caching_device=caching_device):
            v = variable_scope.get_variable("v", [])
            self.assertTrue(v.value().device.startswith(caching_device))

            with variable_scope.variable_scope("child"):
                v2 = variable_scope.get_variable("v", [])
                self.assertTrue(v2.value().device.startswith(caching_device))

            with variable_scope.variable_scope("not_cached", caching_device=""):
                v2_not_cached = variable_scope.get_variable("v", [])
                self.assertFalse(
                    v2_not_cached.value().device.startswith(caching_device))

            with variable_scope.variable_scope(
                "not_cached_identity_device",
                caching_device=lambda op: op.device):
                v2_identity_device = variable_scope.get_variable("v", [])
                self.assertFalse(
                    v2_identity_device.value().device.startswith(caching_device))

            with variable_scope.variable_scope("we_will_do_it_live") as vs_live:
                vs_live.set_caching_device("/job:live")
                v_live = variable_scope.get_variable("v", [])
                self.assertTrue(v_live.value().device.startswith("/job:live"))

        v_tower = variable_scope.get_variable("v", [])
        self.assertFalse(v_tower.value().device.startswith(caching_device))
