import subprocess
import pandas as pd

# Specify the path to your Jupyter Notebook file
notebook_file = 'negotiation.ipynb'

# Specify the number of times to run the notebook
num_runs = 15

# Initialize an empty DataFrame to collect results
results_df = pd.DataFrame(columns=['Iteration', 'Input Generate Time', 'Profile Generate Time', 'Task Generate Time', 'Task Implications Time', 'Sender Offer Generation Time', 'Receiver Offer Generation Time', 'Decision-making Time', 'Running Time', 'Total Rounds', 'Input', 'Mapping', 'Sender', 'A_yes_counts', 'B_yes_counts'])

for i in range(num_runs):
    print(f"Running iteration {i + 1}")
    subprocess.run(['jupyter', 'nbconvert', '--execute', '--to', 'notebook', '--inplace', notebook_file])
    df = pd.read_csv('output.csv')
    df['Iteration'] = i + 1
    print(f"Data collected in iteration {i + 1}:\n{df}")
    results_df = pd.concat([results_df, df], ignore_index=True)

# specify teh name your file
results_df.to_csv('name of the csv file', index=False)

