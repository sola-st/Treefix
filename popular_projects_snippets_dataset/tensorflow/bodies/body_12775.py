# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/candidate_sampling_ops.py
"""Samples a set of classes using a uniform base distribution.

  This operation randomly samples a tensor of sampled classes
  (`sampled_candidates`) from the range of integers `[0, range_max)`.

  See the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf)
  for a quick course on Candidate Sampling.

  The elements of `sampled_candidates` are drawn without replacement
  (if `unique=True`) or with replacement (if `unique=False`) from
  the base distribution.

  The base distribution for this operation is the uniform distribution
  over the range of integers `[0, range_max)`.

  In addition, this operation returns tensors `true_expected_count`
  and `sampled_expected_count` representing the number of times each
  of the target classes (`true_classes`) and the sampled
  classes (`sampled_candidates`) is expected to occur in an average
  tensor of sampled classes. These values correspond to `Q(y|x)`
  defined in the [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf).
  If `unique=True`, then these are post-rejection probabilities and we
  compute them approximately.

  Note that this function (and also other `*_candidate_sampler`
  functions) only gives you the ingredients to implement the various
  Candidate Sampling algorithms listed in the big table in the
  [Candidate Sampling Algorithms
  Reference](http://www.tensorflow.org/extras/candidate_sampling.pdf). You
  still need to implement the algorithms yourself.

  For example, according to that table, the phrase "negative samples"
  may mean different things in different algorithms. For instance, in
  NCE, "negative samples" means `S_i` (which is just the sampled
  classes) which may overlap with true classes, while in Sampled
  Logistic, "negative samples" means `S_i - T_i` which excludes the
  true classes. The return value `sampled_candidates` corresponds to
  `S_i`, not to any specific definition of "negative samples" in any
  specific algorithm. It's your responsibility to pick an algorithm
  and calculate the "negative samples" defined by that algorithm
  (e.g. `S_i - T_i`).

  As another example, the `true_classes` argument is for calculating
  the `true_expected_count` output (as a by-product of this function's
  main calculation), which may be needed by some algorithms (according
  to that table). It's not for excluding true classes in the return
  value `sampled_candidates`. Again that step is algorithm-specific
  and should be carried out by you.

  Args:
    true_classes: A `Tensor` of type `int64` and shape `[batch_size,
      num_true]`. The target classes.
    num_true: An `int`.  The number of target classes per training example.
    num_sampled: An `int`.  The number of classes to randomly sample. The
      `sampled_candidates` return value will have shape `[num_sampled]`. If
      `unique=True`, `num_sampled` must be less than or equal to `range_max`.
    unique: A `bool`. Determines whether all sampled classes in a batch are
      unique.
    range_max: An `int`. The number of possible classes.
    seed: An `int`. An operation-specific seed. Default is 0.
    name: A name for the operation (optional).

  Returns:
    sampled_candidates: A tensor of type `int64` and shape
      `[num_sampled]`. The sampled classes, either with possible
      duplicates (`unique=False`) or all unique (`unique=True`). As
      noted above, `sampled_candidates` may overlap with true classes.
    true_expected_count: A tensor of type `float`.  Same shape as
      `true_classes`. The expected counts under the sampling distribution
      of each of `true_classes`.
    sampled_expected_count: A tensor of type `float`. Same shape as
      `sampled_candidates`. The expected counts under the sampling distribution
      of each of `sampled_candidates`.
  """
seed1, seed2 = random_seed.get_seed(seed)
exit(gen_candidate_sampling_ops.uniform_candidate_sampler(
    true_classes, num_true, num_sampled, unique, range_max, seed=seed1,
    seed2=seed2, name=name))
