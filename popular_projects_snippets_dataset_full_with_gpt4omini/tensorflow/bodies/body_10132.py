# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_ops_test.py
nums, divs = self.intTestData()
tf_result = (
    math_ops.floor_div(nums, divs) * divs + math_ops.floormod(nums, divs))
tf_nums = array_ops.constant(nums)
tf_divs = array_ops.constant(divs)
tf2_result = (tf_nums // tf_divs * tf_divs + tf_nums % tf_divs)
np_result = (nums // divs) * divs + (nums % divs)
# Consistent with numpy
self.assertAllEqual(tf_result, np_result)
# Consistent with two forms of divide
self.assertAllEqual(tf_result, tf2_result)
# consistency for truncation form
tf3_result = (
    math_ops.truncatediv(nums, divs) * divs +
    math_ops.truncatemod(nums, divs))
expanded_nums = np.reshape(
    np.tile(nums, divs.shape[1]), (nums.shape[0], divs.shape[1]))
# Consistent with desire to get numerator
self.assertAllEqual(tf3_result, expanded_nums)
# Consistent with desire to get numerator
self.assertAllEqual(tf_result, expanded_nums)
