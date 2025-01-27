# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
fig = self.plt.figure()
ax = fig.add_subplot(211)

# ts
df = tm.makeTimeDataFrame()
df.plot(secondary_y=["A", "B"], ax=ax)
leg = ax.get_legend()
assert len(leg.get_lines()) == 4
assert leg.get_texts()[0].get_text() == "A (right)"
assert leg.get_texts()[1].get_text() == "B (right)"
assert leg.get_texts()[2].get_text() == "C"
assert leg.get_texts()[3].get_text() == "D"
assert ax.right_ax.get_legend() is None
colors = set()
for line in leg.get_lines():
    colors.add(line.get_color())

# TODO: color cycle problems
assert len(colors) == 4
self.plt.close(fig)

fig = self.plt.figure()
ax = fig.add_subplot(211)
df.plot(secondary_y=["A", "C"], mark_right=False, ax=ax)
leg = ax.get_legend()
assert len(leg.get_lines()) == 4
assert leg.get_texts()[0].get_text() == "A"
assert leg.get_texts()[1].get_text() == "B"
assert leg.get_texts()[2].get_text() == "C"
assert leg.get_texts()[3].get_text() == "D"
self.plt.close(fig)

fig, ax = self.plt.subplots()
df.plot(kind="bar", secondary_y=["A"], ax=ax)
leg = ax.get_legend()
assert leg.get_texts()[0].get_text() == "A (right)"
assert leg.get_texts()[1].get_text() == "B"
self.plt.close(fig)

fig, ax = self.plt.subplots()
df.plot(kind="bar", secondary_y=["A"], mark_right=False, ax=ax)
leg = ax.get_legend()
assert leg.get_texts()[0].get_text() == "A"
assert leg.get_texts()[1].get_text() == "B"
self.plt.close(fig)

fig = self.plt.figure()
ax = fig.add_subplot(211)
df = tm.makeTimeDataFrame()
ax = df.plot(secondary_y=["C", "D"], ax=ax)
leg = ax.get_legend()
assert len(leg.get_lines()) == 4
assert ax.right_ax.get_legend() is None
colors = set()
for line in leg.get_lines():
    colors.add(line.get_color())

# TODO: color cycle problems
assert len(colors) == 4
self.plt.close(fig)

# non-ts
df = tm.makeDataFrame()
fig = self.plt.figure()
ax = fig.add_subplot(211)
ax = df.plot(secondary_y=["A", "B"], ax=ax)
leg = ax.get_legend()
assert len(leg.get_lines()) == 4
assert ax.right_ax.get_legend() is None
colors = set()
for line in leg.get_lines():
    colors.add(line.get_color())

# TODO: color cycle problems
assert len(colors) == 4
self.plt.close()

fig = self.plt.figure()
ax = fig.add_subplot(211)
ax = df.plot(secondary_y=["C", "D"], ax=ax)
leg = ax.get_legend()
assert len(leg.get_lines()) == 4
assert ax.right_ax.get_legend() is None
colors = set()
for line in leg.get_lines():
    colors.add(line.get_color())

# TODO: color cycle problems
assert len(colors) == 4
