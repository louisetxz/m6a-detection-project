# m6a-detection-project

# Table of Contents
- **[Overview](#overview)**<br>
- **[Quick Start Guide](#quick-start-guide)**<br>
    - **[Ubuntu setup](#ubuntu-setup)**<br>
    - **[Cloning the repository](#cloning-the-repository)**<br>
    - **[Installing dependencies](#installing-dependencies)**<br>
- **[Usage](#usage)**<br>
- **[Interpretation](#interpretation)**<br>
- **[Citing](#citing)**<br>
- **[License](#license)**<br>

# Overview
This project aims to address these challenges by developing a robust machine-learning classifier for identifying m6A modifications in RNA-Seq data, specifically focusing on human cell lines from the SG-NEx Project (2021). By enhancing our ability to detect m6A modifications, we hope to contribute to a deeper understanding of m6A's role in cancer and its potential as a target for therapeutic intervention.

# Quick Start Guide

## Ubuntu setup
1. Start an Ubuntu instance from ResearchGateway. A recommended and sufficient Ubuntu instance is: t3.medium
2. Access your Ubuntu instance.

## Cloning the repository
1. Clone the repository. To clone our repository using HTTPS, run
```bash
git clone https://github.com/louisetxz/m6a-detection-project.git
```
2. Change directory into our project.
```
cd m6a-detection-project
```

## Installing dependencies
To update package list, run
```bash
sudo apt-get update
```
To install package manager PIP, run
```bash
sudo apt install python3-pip
```
To install dependencies, run
```bash
pip install -r requirements.txt
```

## Usage
There are two ways you can generate predictions using our model:

1. To generate predictions on the available test data, run:
```bash
python3 test.py
```

2. To generate predictions with your own command-line arguments:
    1. Place test data under data/

    2. Run:
    ```bash
    python3 test.py --model_path /path/to/model --data_path /path/to/data --n 5 --output_filename model_output_datetime.csv
    ```

    The testing script contains the following command-line arguments:
    * --model_path (str): Path to the trained model file. Default is cnn_selected.keras.

    * --data_path (str): Path to the test dataset file which must be in json format. Default is /data/test_data.json.

    * --n (int): Number of prediction rows to print to the console. Default is 10.

    * --output_filename (str): File name for the output predictions. This will save the results to the specified file in the /output directory. Default is model_output_datetime.csv.

## Intepretation of outputs
The output file `model_output_datetime.csv` will be under /output/. It contains the probability of modification at each individual position for each transcript. 

```bash
cd output
```

```bash
cat model_output_datetime.csv
```

The output file will have 3 columns

* ``transcript_id``: The transcript id of the predicted position
* ``transcript_position``: The transcript position of the predicted position
* ``score``: The probability that a given site is modified

# Citing
If you use this mdoel in your research, please cite this repository:
```
@misc{Louise_Tan_and_Khine_Ezali_and_Sean_Lim_and_Rachel_Sitoh_m6a-detection-project_2024,
    author = {Louise Tan and Khine Ezali and Sean Lim and Rachel Sitoh},
    license = {MIT},
    month = nov,
    title = {{m6a-detection-project}},
    url = {https://github.com/louisetxz/m6a-detection-project},
    version = {1},
    year = {2024}
}
```
Or cite Louise Tan, Khine Ezali, Sean Lim, & Rachel Sitoh. (2024). m6a-detection-project (Version 1) [CNN Model]. https://github.com/louisetxz/m6a-detection-project/tree/main

# License
m6Anet is licensed under the terms of the MIT license.