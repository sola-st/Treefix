import os
import pandas as pd

from matplotlib import pyplot as plt

#folder_path = "./metrics_full_datasets_with_GPT4o/random_functions/GPTValuePredictor/raw"

folder_path = "./metrics_full_datasets_with_GPT4o/so_snippets/GPTValuePredictor/raw"

files = os.listdir(folder_path)
files = [file for file in files if file.startswith("metrics_") and file.endswith(".csv")]

# explored_nodes = {}

# for file in files:
#     df = pd.read_csv(f'{folder_path}/{file}')
#     file_name = df.iloc[0]['file']

#     explored_nodes[file_name] = {}

#     explored_nodes[file_name]['initial'] = df.iloc[0]['num_executions']
#     explored_nodes[file_name]['refine'] = df.iloc[1]['num_executions']
#     explored_nodes[file_name]['guide'] = df.iloc[2]['num_executions']

# file = []
# initial = []
# refine = []
# guide = []

# for f in explored_nodes.keys():
#     file.append(f)
#     initial.append(explored_nodes[f]['initial'])
#     refine.append(explored_nodes[f]['refine'])
#     guide.append(explored_nodes[f]['guide'])

# explored_nodes_dataset = pd.DataFrame({
#     'file': file,
#     'initial': initial,
#     'refine': refine,
#     'guide': guide
# })
# explored_nodes_dataset.to_csv('explored_nodes.csv', index=False)

file_name = []
nodes = []
initial = []
refine = []
guide = []
nodes_in_P = []
p_location = []
full_coverage_initial = 0
executed_refine = 0
executed_guide = 0
for file in files:
    df = pd.read_csv(f'{folder_path}/{file}')
    name = df.iloc[0]['file']
    file_name.append(name)
    nodes.append(df.iloc[0]['num_executions'] + df.iloc[1]['num_executions'] + df.iloc[2]['num_executions'])
    initial.append(df.iloc[0]['num_executions'])
    refine.append(df.iloc[1]['num_executions'])
    guide.append(df.iloc[2]['num_executions'])
    nodes_in_P.append(df.iloc[2]['minimal_predictions_set_size'])

    if df.iloc[1]['num_executions'] == 0 and df.iloc[2]['num_executions'] == 0:
        full_coverage_initial += 1
    if df.iloc[1]['num_executions'] > 0:
        executed_refine += 1
    if df.iloc[2]['num_executions'] > 0:
        executed_guide += 1

    max_coverage_prediction = str(df.iloc[2]['max_coverage_prediction'])
    if 'initial' in max_coverage_prediction:
        p_location.append('initial')
    elif 'refine' in max_coverage_prediction:
        p_location.append('refine')
    elif 'guide' in max_coverage_prediction:
        p_location.append('guide')

explored_nodes_dataset = pd.DataFrame({
    'file': file_name,
    'All': nodes,
    'Step 1': initial,
    'Step 2': refine,
    'Step 3': guide,
    '∈ P': nodes_in_P
})
explored_nodes_dataset.to_csv('explored_nodes.csv', index=False)

# Plot histogram and get min, max, avg values.

meanlineprops = dict(linestyle='--', linewidth=4, color='black')
medianlineprops = dict(linestyle='-', linewidth=4, color='gray')
flierprops = dict(marker='+',markerfacecolor='gray', markersize=12,
                  linestyle='none', markeredgecolor='gray')

#plt.figure(figsize=(36,6))
explored_nodes_dataset.plot.box(
    showmeans=True, meanprops=meanlineprops, meanline=True,
    medianprops=medianlineprops,
   # vert=0,
    flierprops=flierprops);

plt.rcParams.update({'font.size': 35})
plt.rcParams["figure.figsize"] = (15,15)
plt.xticks(fontsize=35)
plt.yticks(fontsize=35)
plt.ylabel("Prefixes", fontsize=35)
#plt.xlabel("Step")
plt.plot([], [], '--', linewidth=4, color='black', label='mean')
plt.plot([], [], '-', linewidth=4, color='gray', label='median')
#plt.plot([], [], 'x', markersize=12, color='gray', label='fliers')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.25), ncol=2)
plt.gcf().set_size_inches(12, 6)
plt.savefig("explored_nodes.pdf", bbox_inches = "tight")
#files.download("fcts_dataset_execution_time_per_step.pdf")

print(explored_nodes_dataset.describe(include='all'))

print(p_location.count('initial'))
print(p_location.count('guide'))
print(p_location.count('refine'))

print(refine.count(0))
print(guide.count(0))

print(f"Snippets with 100% coverage on step 1: {full_coverage_initial}")
print(f"Snippets that went to step 2: {executed_refine}")
print(f"Snippets that went to step 3: {executed_guide}")
