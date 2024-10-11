# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/nadam.py
lr_t = array_ops.identity(self._get_hyper('learning_rate', var_dtype))
beta_1_t = array_ops.identity(self._get_hyper('beta_1', var_dtype))
beta_2_t = array_ops.identity(self._get_hyper('beta_2', var_dtype))
local_step = math_ops.cast(self.iterations + 1, var_dtype)
next_step = math_ops.cast(self.iterations + 2, var_dtype)

decay_base = math_ops.cast(0.96, var_dtype)

m_t = beta_1_t * (1. - 0.5 * (
    math_ops.pow(decay_base, self._initial_decay * local_step)))
m_t_1 = beta_1_t * (1. - 0.5 * (
    math_ops.pow(decay_base, self._initial_decay * next_step)))

m_schedule_new = math_ops.cast(self._m_cache_read, var_dtype) * m_t
if var_dtype is self._m_cache.dtype:
    m_schedule_new = array_ops.identity(state_ops.assign(
        self._m_cache, m_schedule_new, use_locking=self._use_locking))
m_schedule_next = m_schedule_new * m_t_1

apply_state[(var_device, var_dtype)] = dict(
    lr_t=lr_t,
    neg_lr_t=-lr_t,  # pylint: disable=invalid-unary-operand-type
    epsilon=ops.convert_to_tensor_v2_with_dispatch(self.epsilon, var_dtype),
    beta_1_t=beta_1_t,
    beta_2_t=beta_2_t,
    m_t=m_t,
    m_t_1=m_t_1,
    one_minus_beta_1_t=1 - beta_1_t,
    one_minus_beta_2_t=1 - beta_2_t,
    one_minus_m_t=1. - m_t,
    one_minus_m_schedule_new=1. - m_schedule_new,
    one_minus_m_schedule_next=1. - m_schedule_next,
    v_t_prime_denominator=1. - math_ops.pow(beta_2_t, local_step),
)
