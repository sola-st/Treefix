# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/gradient_input_output_exclusions.py
"""Generates lookup function with given name and lookup table entries."""
contents = """
absl::optional<tensorflow::gtl::FlatSet<int>> {name}(
    const tensorflow::string &op_name) {{
  static std::array<OpIndexInfo, {count}> a = {{{{
""".format(
  name=name, count=len(entries) + 1)
contents += "      "
contents += "\n      ".join(entries[op_type] for op_type in sorted(entries))
contents += "\n      {\"VarHandleOp\"},"
contents += """
  }};
  static const auto &m = *OpGradientInfoInit(a);

  auto it = m.find(op_name);
  if (it != m.end()) {
    return it->second;
  }
  return absl::nullopt;
}
"""
exit(contents)
