# Ethics-based Negotiation
Replication package of the study on ethics-based negotiation between two autonomous agents where each agent represents a user and utilizes its ethical prefrences for ethical decision-making.

This study has been designed, developed, and reported by the following investigators:

- [Mashal Afzal Memon](https://scholar.google.com/citations?user=Mnu_k-8AAAAJ&hl=en) (University of L'Aquila, Italy)
- [Gian Luca Scoccia](https://scholar.google.com/citations?user=y8EX4DAAAAAJ&hl=en) (Gran Sasso Science Institute, Italy)
- [Marco Autili](https://scholar.google.com/citations?user=s8F7eWIAAAAJ&hl=en&oi=ao) (University of L'Aquila, Italy)
- [Paola Inverardi](https://scholar.google.com/citations?user=x8XlRFgAAAAJ&hl=en&oi=ao) (Gran Sasso Science Institute, Italy)

For any information, interested researchers can contact us by writing an email to [mashalafzal.memon@graduate.univaq.it](mailto:mashalafzal.memon@graduate.univaq.it)

# Structure of the replication package
This replication package is organized according to the following structure.
```
1. readme.md                    # the file you are reading right now.

2. running code                 # a folder containing the python scripts to perform the experiment.

2.1 all_functions.py            # a python script containing functions to generate the required input and other functions to carry on the negotiation. This script is self-contained, it does not depend on other scripts.
2.2 negotiation.ipynb           # a jupyter notebook containing the main negotiation class. This notebook is dependent on the all_functions.py script.
2.3 loop.py                     # a python script containing a loop to perform the negotiation for desired number of iterations and record the data of entire negotiation process in a combined csv file.

3. results                      # a folder containing results of the experiment performed on various input size.

3.1 mapping1to5                 # a folder contatinig results fo the negotiation process where the ethical principles are ranked between 1 and 5.

3.1.1 best_mapping1to5.pdf      # a PDF file containing results of negotiation process where each agent follows the tactic to send an offer randomly from its 10% of best offers according to its own ethical profile.
3.1.2 max_mapping1to5.pdf       # a PDF file containing results of negotiation process where each agent follows the tactic to send the offer that has maximum utility according to its own ethical profile.
3.1.3 random_mapping1to5.pdf    # a PDF file containing results of negotiation process where each agent follows the tactic to send an offer randomly from all posisble alternatives.

3.2 mapping1to50                # a folder contatinig results fo the negotiation process where the ethical principles are ranked between 1 and 50.

3.2.1 mapping1to50.pdf          # a PDF file containing results of negotiation process where each agent follows the tactic to send an offer randomly from its 10% of best offers according to its own ethical profile.

3.3 mapping1to1000              # a folder contatinig results fo the negotiation process where the ethical principles are ranked between 1 and 1000.

3.3.1 mapping1to1000.pdf        # a PDF file containing results of negotiation process where each agent follows the tactic to send an offer randomly from its 10% of best offers according to its own ethical profile. 
