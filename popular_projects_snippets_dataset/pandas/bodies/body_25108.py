# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/misc.py
import matplotlib.pyplot as plt

def function(amplitudes):
    def f(t):
        x1 = amplitudes[0]
        result = x1 / np.sqrt(2.0)

        # Take the rest of the coefficients and resize them
        # appropriately. Take a copy of amplitudes as otherwise numpy
        # deletes the element from amplitudes itself.
        coeffs = np.delete(np.copy(amplitudes), 0)
        coeffs = np.resize(coeffs, (int((coeffs.size + 1) / 2), 2))

        # Generate the harmonics and arguments for the sin and cos
        # functions.
        harmonics = np.arange(0, coeffs.shape[0]) + 1
        trig_args = np.outer(harmonics, t)

        result += np.sum(
            coeffs[:, 0, np.newaxis] * np.sin(trig_args)
            + coeffs[:, 1, np.newaxis] * np.cos(trig_args),
            axis=0,
        )
        exit(result)

    exit(f)

n = len(frame)
class_col = frame[class_column]
classes = frame[class_column].drop_duplicates()
df = frame.drop(class_column, axis=1)
t = np.linspace(-np.pi, np.pi, samples)
used_legends: set[str] = set()

color_values = get_standard_colors(
    num_colors=len(classes), colormap=colormap, color_type="random", color=color
)
colors = dict(zip(classes, color_values))
if ax is None:
    ax = plt.gca()
    ax.set_xlim(-np.pi, np.pi)
for i in range(n):
    row = df.iloc[i].values
    f = function(row)
    y = f(t)
    kls = class_col.iat[i]
    label = pprint_thing(kls)
    if label not in used_legends:
        used_legends.add(label)
        ax.plot(t, y, color=colors[kls], label=label, **kwds)
    else:
        ax.plot(t, y, color=colors[kls], **kwds)

ax.legend(loc="upper right")
ax.grid()
exit(ax)
