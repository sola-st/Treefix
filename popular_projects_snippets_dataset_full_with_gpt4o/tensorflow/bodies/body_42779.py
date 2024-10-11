# Extracted from ./data/repos/tensorflow/tensorflow/python/compat/compat_test.py
var_name = 'TF_FORWARD_COMPATIBILITY_DELTA_DAYS'

def remove_os_environment_var():
    try:
        del os.environ[var_name]
    except KeyError:
        pass

self.addCleanup(remove_os_environment_var)

compatibility_date = self._compatibility_date()
one_day_before = self._n_days_after(-1)
one_day_after = self._n_days_after(1)
ten_days_after = self._n_days_after(10)
nine_days_after = self._n_days_after(9)

self.assertTrue(compat.forward_compatible(*one_day_before))
self.assertFalse(compat.forward_compatible(*compatibility_date))
self.assertFalse(compat.forward_compatible(*one_day_after))
self.assertFalse(compat.forward_compatible(*nine_days_after))
self.assertFalse(compat.forward_compatible(*ten_days_after))

os.environ[var_name] = '10'
compat._update_forward_compatibility_date_number()
self.assertTrue(compat.forward_compatible(*one_day_before))
self.assertTrue(compat.forward_compatible(*compatibility_date))
self.assertTrue(compat.forward_compatible(*one_day_after))
self.assertTrue(compat.forward_compatible(*nine_days_after))
self.assertFalse(compat.forward_compatible(*ten_days_after))

del os.environ[var_name]
compat._update_forward_compatibility_date_number()
self.assertTrue(compat.forward_compatible(*one_day_before))
self.assertFalse(compat.forward_compatible(*compatibility_date))
self.assertFalse(compat.forward_compatible(*one_day_after))
self.assertFalse(compat.forward_compatible(*nine_days_after))
self.assertFalse(compat.forward_compatible(*ten_days_after))

# Now test interaction between environment variable and context func.
os.environ[var_name] = '10'
compat._update_forward_compatibility_date_number()
self.assertTrue(compat.forward_compatible(*one_day_after))
with compat.forward_compatibility_horizon(*one_day_after):
    self.assertTrue(compat.forward_compatible(*one_day_before))
    self.assertTrue(compat.forward_compatible(*compatibility_date))
    self.assertFalse(compat.forward_compatible(*one_day_after))
    self.assertFalse(compat.forward_compatible(*nine_days_after))
    self.assertFalse(compat.forward_compatible(*ten_days_after))
self.assertTrue(compat.forward_compatible(*one_day_after))
