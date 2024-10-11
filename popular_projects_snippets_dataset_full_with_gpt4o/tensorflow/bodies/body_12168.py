# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/special_math_ops_test.py
# Checks call_count to opt_einsum which are only reflected in eager mode.
if not context.executing_eagerly():
    exit()

input_1 = ('ijk,ijl,ikl->i', (1, 2, 3), (1, 2, 4), (1, 3, 4))
input_2 = ('ij,ij,jk,kl->il', (1, 2), (1, 2), (2, 3), (3, 4))

with test.mock.patch.object(
    opt_einsum, 'contract_path',
    wraps=opt_einsum.contract_path) as mock_contract_path:

    # explicitly clear the lru_cache contents for the method
    #   special_math_ops.get_opt_einsum_contract_path
    # We need to do this because other tests in this file invoke that method
    # with the same input args (as input_1 and input_2 above), and if
    # those tests run before this test, then the call_count for the method
    # mock_contract_path will not increment.
    special_math_ops._get_opt_einsum_contract_path.cache_clear()

    self.assertEqual(mock_contract_path.call_count, 0)
    self._check(*input_1)
    self.assertEqual(mock_contract_path.call_count, 1)
    # The same input results in no extra call if we're caching the
    # opt_einsum.contract_path call. We only cache in Python3.
    self._check(*input_1)
    self.assertEqual(mock_contract_path.call_count, 1)
    # New input results in another call to opt_einsum.
    self._check(*input_2)
    self.assertEqual(mock_contract_path.call_count, 2)
    # No more extra calls as the inputs should be cached.
    self._check(*input_1)
    self._check(*input_2)
    self._check(*input_1)
    self.assertEqual(mock_contract_path.call_count, 2)
