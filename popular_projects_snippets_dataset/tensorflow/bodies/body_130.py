# Extracted from ./data/repos/tensorflow/tensorflow/tools/build_info/gen_build_info.py
"""Writes a Python that describes the build.

  Args:
    filename: filename to write to.
    key_value_list: A list of "key=value" strings that will be added to the
      module's "build_info" dictionary as additional entries.
  """

build_info = {}

if cuda_config:
    build_info.update(cuda_config.config)

if tensorrt_config:
    build_info.update(tensorrt_config.config)

for arg in key_value_list:
    key, value = arg.split("=")
    if value.lower() == "true":
        build_info[key] = True
    elif value.lower() == "false":
        build_info[key] = False
    else:
        build_info[key] = value.format(**build_info)

  # Sort the build info to ensure deterministic output.
sorted_build_info_pairs = sorted(build_info.items())

contents = """
# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
\"\"\"Auto-generated module providing information about the build.\"\"\"
import collections

build_info = collections.OrderedDict(%s)
""" % sorted_build_info_pairs
open(filename, "w").write(contents)
