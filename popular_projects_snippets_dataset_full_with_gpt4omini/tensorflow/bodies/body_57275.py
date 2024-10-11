# Extracted from ./data/repos/tensorflow/tensorflow/lite/experimental/acceleration/compatibility/convert_binary_to_cc_source.py
"""Returns strings representing a C++ constant array containing `data`.

  Args:
    data: Byte array that will be converted into a C++ constant.
    array_name: String to use as the variable name for the constant array.
    max_line_width: The longest line length, for formatting purposes.
    include_guard: Name to use for the include guard macro definition.
    include_path: Optional path to include in the source file.
    use_tensorflow_license: Whether to include the standard TensorFlow Apache2
      license in the generated files.

  Returns:
    Text that can be compiled as a C++ source file to link in the data as a
    literal array of values.
    Text that can be used as a C++ header file to reference the literal array.
  """

starting_pad = "   "
array_lines = []
array_line = starting_pad
for value in bytearray(data):
    if (len(array_line) + 4) > max_line_width:
        array_lines.append(array_line + "\n")
        array_line = starting_pad
    array_line += " 0x%02x," % value
if len(array_line) > len(starting_pad):
    array_lines.append(array_line + "\n")
array_values = "".join(array_lines)

if include_guard is None:
    include_guard = "TENSORFLOW_LITE_UTIL_" + array_name.upper() + "_DATA_H_"

if include_path is not None:
    include_line = "#include \"{include_path}\"\n".format(
        include_path=include_path)
else:
    include_line = ""

if use_tensorflow_license:
    license_text = """
/* Copyright {year} The TensorFlow Authors. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
==============================================================================*/
""".format(year=datetime.date.today().year)
else:
    license_text = ""

source_template = """{license_text}
// This is a binary file that has been converted into a C++ data array using the
// //tensorflow/lite/experimental/acceleration/compatibility/convert_binary_to_cc_source.py
// script. This form is useful for compiling into a binary to simplify
// deployment on mobile devices

{include_line}
// We need to keep the data array aligned on some architectures.
#ifdef __has_attribute
#define HAVE_ATTRIBUTE(x) __has_attribute(x)
#else
#define HAVE_ATTRIBUTE(x) 0
#endif
#if HAVE_ATTRIBUTE(aligned) || (defined(__GNUC__) && !defined(__clang__))
#define DATA_ALIGN_ATTRIBUTE __attribute__((aligned(16)))
#else
#define DATA_ALIGN_ATTRIBUTE
#endif

extern const unsigned char {array_name}[] DATA_ALIGN_ATTRIBUTE = {{
{array_values}}};
extern const int {array_name}_len = {array_length};
"""

source_text = source_template.format(
    array_name=array_name,
    array_length=len(data),
    array_values=array_values,
    license_text=license_text,
    include_line=include_line)

header_template = """
{license_text}

// This is a binary file that has been converted into a C++ data array using the
// //tensorflow/lite/experimental/acceleration/compatibility/convert_binary_to_cc_source.py
// script. This form is useful for compiling into a binary to simplify
// deployment on mobile devices

#ifndef {include_guard}
#define {include_guard}

extern const unsigned char {array_name}[];
extern const int {array_name}_len;

#endif  // {include_guard}
"""

header_text = header_template.format(
    array_name=array_name,
    include_guard=include_guard,
    license_text=license_text)

exit((source_text, header_text))
