# RAMP starting kit on the Fraud detection

Authors: Miaobing Chen, Anderson Carlos Ferreira da Silva, Pawel Guzewicz


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
This will create the following tree structure
```
fraud_detection/
├── data
│   ├── sample_submission.csv
│   ├── test.csv
│   └── train.csv
├── data_preparation.ipynb
├── fraud_detection_starting_kit.ipynb
├── kaggle_data
│   └── README.md
├── prepare_data.py
├── problem.py
├── README.md
├── requirements.txt
└── submissions
    └── starting_kit
        ├── classifier.py
        └── feature_extractor.py
```
Execute
```
ramp_test_submission --quick-test
```
to test `submissions/starting_kit/feature_extractor.py` and `submissions/starting_kit/classifier.py` against the mock data in `data/`.

Read fraud_detection/kaggle_data/README.md and download the Kaggle dataset
```
fraud_detection/
...
├── kaggle_data
│   └── fraud_detection.csv
└── ...
```
Once the data is in place, execute
```
python prepare_data.py
```
or run [data preparation notebook](data_preparation.ipynb)
and afterwards check
```
ramp_test_submission
```
If it runs and print training and test errors on each fold, then your setup is complete.

Please refer to the corresponding sections in the [starting kit notebook](fraud_detection_starting_kit.ipynb) for more information about submitting to RAMP.
