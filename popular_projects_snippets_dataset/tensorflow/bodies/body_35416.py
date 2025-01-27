# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/parameterized_truncated_normal_op_test.py
"""Calculates the truncated normal moments.

    Args:
      moment: The number for the moment.

    Returns:
      The value for the given moment.

    Uses the recurrence relation described in:
        http://www.smp.uq.edu.au/people/YoniNazarathy/teaching_projects
            /studentWork/EricOrjebin_TruncatedNormalMoments.pdf
    """
assert moment > 0
# The test case must ensure it can import scipy.stats before this point.
import scipy.stats  # pylint: disable=g-import-not-at-top
dist = scipy.stats.norm(loc=self.mean, scale=self.stddev)
for k in range(len(self.memoized_moments), moment + 1):
    m_k_minus_2 = self.memoized_moments[k - 2] if k > 1 else np.double(0.0)
    m_k_minus_1 = self.memoized_moments[k - 1]
    numerator = (np.power(self.maxval, k - 1) * dist.pdf(self.maxval) -
                 np.power(self.minval, k - 1) * dist.pdf(self.minval))
    denominator = dist.cdf(self.maxval) - dist.cdf(self.minval)
    m = ((k - 1) * self.stddev**2 * m_k_minus_2 + self.mean * m_k_minus_1 -
         self.stddev * numerator / denominator)
    assert abs(m) < 1e50  # ensure numerical accuracy
    self.memoized_moments.append(m)
exit(self.memoized_moments[moment])
