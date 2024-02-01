# Ethics-based Negotiation
Replication package of ethics-based negotiation approach in which autonomous systems utilize their user's ethical preferences to negotiate with each other and reach an agreement that satisfies ethical beliefs of all parties involved.

![parking](https://github.com/mashalafzal/Ethics-based-Negotiation/assets/99733316/fc0b4adc-9651-471c-acb9-dc8bc8fd4574)

--The user uploads their ethical profile through a companion application. The ethical profile is used by the autonomous system to control its autonomy. The user also specify the goal. In this case, the autonomous system is the autonomous vehicle and the goal is to drive the passenger to a specific destination.

--The autonomous vehicle drive and reach at the destination specifies by its passenger and finds an available parking. The other vehicle carrying another passenger is also trying to get the same available parking space.

--Both autonomous vehicles negotiate with each other to claim available parking space. 

--The vehicles evaluates the exchange of offers based on their passenger's ethical profile untill an agreement is reached or any of them quit the negotiation.

--When teh agreemnet is reached, one of the vehicles claim the availble parking space and the other vehicle looks for the new parking space.



# Structure of the replication package
This replication package is organized according to the following structure.
```
1. readme.md                              # the file you are reading right now.

2. running code                           # a folder containing the python scripts to perform the experiment.

2.1 all_functions.py                      # a python script containing functions to generate the required input and supported functions to carry on the negotiation. This script is self-contained, it does not depend on any other script.
2.2 negotiation.ipynb                     # a jupyter notebook containing the main negotiation class. This notebook is dependent on the all_functions.py.
2.3 loop.py                               # a python script containing a loop to perform the negotiation for desired number of iterations. It records the data of entire negotiation process in a combined csv file. This script is dependent on negotiation.ipynb and all_functions.py.
2.4 plots.ipynb                           # a jupyter notebook containing the code to generate box plots of outcome of ethics-based negotiation.

3. iteration data                         # a folder containing csv files obtained through each iteration during negotiation.

4. results                                # a folder containing results of the experiment performed on various input size.

4.1 negotiation_rounds.pdf                # a pdf file containing results for the total number of negotiation rounds argued between both autonomous systems at each proportion of input.
4.2 computation_time.pdf                  # a pdf file containing results of the total computation time taken to carry on the experiment at each proportion of input.
4.3 sender_offer_generation_time.pdf      # a pdf file containing result of computation time taken by sender autonomous system for generating and evaluating offers during negotiation at each proportion of input.
4.4 receiver_offer_generation_time.pdf    # a pdf file containing result of computation time taken by receiver autonomous system for generating and evaluating offers during negotiation at each proportion of input.
4.5 decision_making_time.pdf               # a pdf file containing results for the decision-making time before the negotiation concludes at each proportion of input.


```

# How to run the experiment
* To run the experiments, you need Python version 3.9.12 or higher. 
* From running code folder, download all_functions.py, negotiation.ipynb, loop.py files and plots.ipynb.
* In all_functions.py, navigate to the functions generate_user_inputs, generate_profiles and generate_tasks to specify the input size.
* Then, navigate to functions assign_data_to_profiles and create_task_implication to specify the ratio of affected principles.
* To rank ethical principles on your desired scale, modify the generate_profiles to specify the desired range. At the moment, the range is set between 1 to 5.
* In loop.py, specify the num_run to run the experiment for desired number for iterations.
* Run plots.ipynb to generate box plot of ethics-based negotiation at different input size with multiple iterations. Navigate to the directory where your output files are saved.

* To change the tactic for sending offer, modify the negotiation.ipynb. Th desired functions are already predefined in all_functions.py. In negotiation.ipynb, modify find_best_offer as find_random_offer to send any offer randomly from all possible alternatives or as find_max_utility_offer to always send the offer that has high utility among all possible offers.
