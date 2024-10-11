# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition_test.py
rp = rp_factory()
spec = rp._type_spec
actual_components = spec._to_components(rp)
self.assertAllEqual(actual_components, components)
rp_reconstructed = spec._from_components(actual_components)
_assert_row_partition_equal(self, rp, rp_reconstructed)
