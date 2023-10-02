# Ethics-based Negotiation
Replication package of the study on ethics-based negotiation between two autonomous agents where each agent represents a user and utilizes its ethical prefrences for ethical decision-making.

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
