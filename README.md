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
This project aims to address challenges that exist in developing a robust machine-learning classifier for identifying m6A modifications in RNA-Seq data, specifically focusing on cell lines found in the SG-NEx Project (2021). By enhancing our ability to detect m6A modifications, we hope to contribute to a deeper understanding of identification of m6A and its potential as a target for therapeutic intervention.

# Quick Start Guide

## Ubuntu setup
1. Start an Ubuntu instance from ResearchGateway. A recommended and sufficient Ubuntu instance is: t3.medium.
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
Note: These dependencies are required only for the testing file, `test.py`.

## Usage
There are two ways you can generate predictions using our model:

- To generate predictions on the **preloaded test data** available in the repository, run:
```bash
python3 test.py
```

- To generate predictions with your own data or your own command-line arguments:
    1. Place your data under data/. The data should follow the format of the direct RNA-Seq data as in the SG-NEx project.

    2. Run:
    ```bash
    python3 test.py --model_path /path/to/model --data_path /path/to/data --n 5 --output_filename your-filename.csv
    ```

    The testing script contains the following command-line arguments:
    * --model_path (str): Path to the trained model file. Default is cnn_selected.h5.

    * --data_path (str): Path to the test dataset file which must be in json format. Default is /data/test_data.json.

    * --n (int): Number of rows of the predictions to print to the console. Default is 10.

    * --output_filename (str): File name for the output predictions. This will save the results to the specified file in the /output folder. Default is model_output_`datetime`.csv, where `datetime` is captured from the server where you are running the code. In an Ubuntu instance, it will follow the UTC timezone.

## Interpretation of outputs
The predictions will be saved as a **csv** file (Default name: `model_output_datetime.csv`) which can be found under the /output folder. It contains the results of modification at each individual position for each transcript. To see the predictions, follow these steps:

1. Navigate to the output directory to locate the file with the prediction results:
```bash
cd output
```
2. List all files in the output directory to identify the latest predictions file:
```bash
ls
```
3. Display the predictions in the terminal by specifying the appropriate filename (e.g., model_output_datetime.csv):
```bash
cat model_output_datetime.csv #Replace with your desired file name
```

The output file will the following three columns:

* ``transcript_id``: The transcript id of the predicted position
* ``transcript_position``: The transcript position of the predicted position
* ``score``: The probability that a given site is modified

# Citing
If you use this model in your research, please cite this repository:
```
@misc{Louise_Tan__Xuan)Zhi_and_Khine_Ezali_and_Lim_Shih_Ler_Sean_and_Sitoh_Ying_Ting_Rachel_m6a-detection-project_2024,
    author = {Louise Tan Xuan Zhi and Khine Ezali and Lim Shih Ler Sean and Sitoh Ying Ting Rachel},
    license = {MIT},
    month = nov,
    title = {{m6a-detection-project}},
    url = {https://github.com/louisetxz/m6a-detection-project},
    version = {1},
    year = {2024}
}
```
Or cite Louise Tan Xuan Zhi, Khine Ezali, Lim Shih Ler Sean, & Sitoh Ying Ting Rachel. (2024). m6a-detection-project (Version 1) [CNN Model]. https://github.com/louisetxz/m6a-detection-project

# License
m6Anet is licensed under the terms of the MIT license.