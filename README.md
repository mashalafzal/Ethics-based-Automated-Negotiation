# Ethics-based Negotiation
Replication package of the study on ethics-based negotiation between two autonomous agents where each agent represents a user and utilizes its ethical preferences to negotiate with other agent for ethical decision-making.

# Structure of the replication package
This replication package is organized according to the following structure.
```
1. readme.md                    # the file you are reading right now.

2. running code                 # a folder containing the python scripts to perform the experiment.

2.1 all_functions.py            # a python script containing functions to generate the required input and other functions to carry on the negotiation. This script is self-contained, it does not depend on other scripts.
2.2 negotiation.ipynb           # a jupyter notebook containing the main negotiation class. This notebook is dependent on the all_functions.py.
2.3 loop.py                     # a python script containing a loop to perform the negotiation for desired number of iterations and record the data of entire negotiation process in a combined csv file. This script is dependent on negotiation.ipynb and all_functions.py.

3. results                      # a folder containing results of the experiment performed on various input size.

3.1 mapping1to5                 # a folder contatinig results fo the negotiation process where the ethical principles are ranked between 1 and 5.
3.2 mapping1to50                # a folder contatinig results fo the negotiation process where the ethical principles are ranked between 1 and 50.
3.3 mapping1to1000              # a folder contatinig results fo the negotiation process where the ethical principles are ranked between 1 and 1000.
```

# How to run the experiment
* To run the experiments, you need Python version 3.9.12 or higher. 
* From running code folder, download all_functions.py, negotiation.ipynb and loop.py files.
* In all_functions.py, navigate to the functions generate_user_inputs, generate_profiles and generate_tasks function and specify the input size.
* Then, navigate to functions assign_data_to_profiles and craete_task_implication to specify the ratio of affected principles.
* To rank ethical principles on your desired range, modify the generate_profiles to specify the desired range.
* In loop.py, specify the num_run to desired number for iterations.
