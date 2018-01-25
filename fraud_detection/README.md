# RAMP starting kit on the Fraud detection

Authors: Anderson_Carlos_Ferreira_da_Silva, Miaobing CHEN, Pawel_Guzewicz


### Quick start
```
pip install git+https://github.com/paris-saclay-cds/ramp-workflow.git
git clone https://github.com/ramp-kits/------
```
Go to [`ramp-workflow`](https://github.com/paris-saclay-cds/ramp-workflow/wiki) for more help on the [RAMP](http:www.ramp.studio) ecosystem.

Get started on this RAMP with the [dedicated notebook](fraud_detection_starting_kit.ipynb).


## Setting up the starting kit

First install `ramp-workflow` (`rampwf`). 
```
pip install git+https://github.com/paris-saclay-cds/ramp-workflow.git
```
Second, install this kit
```
git clone https://github.com/ramp-kits/---
```
This will create the following arborescence
```
fraud_detection/
├── data
│   ├── sample_submission.csv
│   ├── test.csv
│   └── train.csv
├── submissions
│   ├── starting_kit
│   │   ├── classifier.py
│   │   └── feature_extractor.py
├── README.md
├── fraud_detection_starting_kit.ipynb
├── mock_data.py
├── problem.py
└── requirements.txt
```
Execute
```
ramp_test_submission --quick-test
```
to test `submissions/starting_kit/feature_extractor.py` and `submissions/starting_kit/classifier.py` against the mock data in `data/`. If you want to test the starting kit on the official Kaggle data, sign up to the [Kaggle challenge](https://www.kaggle.com/ntnu-testimon/paysim1), download, rename and place it in `kaggle_data/`. 
```
fraud_detection/
...
├── kaggle_data
│   ├── fraud_detection.csv
└── 
```
Once the data is in place, execute
```
ramp_test_submission
```
If it runs and print training and test errors on each fold, then your setup is complete.

Please refer to the corresponding sections in the [notebook](fraud_detection_starting_kit.ipynb) for more information about submitting to RAMP.
