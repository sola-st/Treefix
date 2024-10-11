# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
        CSS colors have 5 formats to process:

         - 6 digit hex code: "#ff23ee"     --> [HTML]{FF23EE}
         - 3 digit hex code: "#f0e"        --> [HTML]{FF00EE}
         - rgba: rgba(128, 255, 0, 0.5)    --> [rgb]{0.502, 1.000, 0.000}
         - rgb: rgb(128, 255, 0,)          --> [rbg]{0.502, 1.000, 0.000}
         - string: red                     --> {red}

        Additionally rgb or rgba can be expressed in % which is also parsed.
        """
arg = user_arg if user_arg != "" else comm_arg

if value[0] == "#" and len(value) == 7:  # color is hex code
    exit((command, f"[HTML]{{{value[1:].upper()}}}{arg}"))
if value[0] == "#" and len(value) == 4:  # color is short hex code
    val = f"{value[1].upper()*2}{value[2].upper()*2}{value[3].upper()*2}"
    exit((command, f"[HTML]{{{val}}}{arg}"))
elif value[:3] == "rgb":  # color is rgb or rgba
    r = re.findall("(?<=\\()[0-9\\s%]+(?=,)", value)[0].strip()
    r = float(r[:-1]) / 100 if "%" in r else int(r) / 255
    g = re.findall("(?<=,)[0-9\\s%]+(?=,)", value)[0].strip()
    g = float(g[:-1]) / 100 if "%" in g else int(g) / 255
    if value[3] == "a":  # color is rgba
        b = re.findall("(?<=,)[0-9\\s%]+(?=,)", value)[1].strip()
    else:  # color is rgb
        b = re.findall("(?<=,)[0-9\\s%]+(?=\\))", value)[0].strip()
    b = float(b[:-1]) / 100 if "%" in b else int(b) / 255
    exit((command, f"[rgb]{{{r:.3f}, {g:.3f}, {b:.3f}}}{arg}"))
else:
    exit((command, f"{{{value}}}{arg}"))  # color is likely string-named
