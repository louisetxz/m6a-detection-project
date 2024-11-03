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
1. Add your SSH key into the Ubuntu instance or create a new one.
To create a new SSH key, follow these steps:
    1. Create a new key.
    ```bash
    ssh-keygen -t rsa -b 4096 -C your_email@example.com (e.g. your github email address)
    ```
    This creates a new SSH key, using the provided email as a label.
    When you're prompted to "Enter a file in which to save the key", you can press Enter to accept the default file location. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key. To do so, type the default file location and replace id_ALGORITHM with your custom key name.
    
    2. At the prompt, type a secure passphrase or empty for none.
    3. Start the ssh-agent.
    ```bash
    eval "$(ssh-agent -s)"
    ```
    4. Add the ssh-agent.
    ```
    ssh-add ~/.ssh/id_rsa
    ```
    5. Read the content of your SSH public key file.
    ```bash
    cat ~/.ssh/id_rsa.pub 
    ```
    Copy the output of this command to be added into GitHub.
    
    6. To add the SSH key to GitHub, login to your GitHub >> Go to Settings >> "SSH and GPG keys" >> New SSH Key >> Add any title >> Paste your copied output into the "Key" field

    7. Test the connection:
    ```bash
    ssh -T git@github.com
    ```

2. Clone the repository. To clone our repository using SSH, run
```bash
git clone git@github.com:louisetxz/m6a-detection-project.git
```
3. Change directory into our project.
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
Now, cd into our github folder
```bash
cd m6a-detection-project
```
To install dependencies, run
```bash
pip install -r requirements.txt
```

## Usage
There are two ways you can generate predictions using our model:

- To generate predictions on the available test data, run:
```bash
python3 test.py
```

- To generate predictions with your own command-line arguments:
1. Place test data under /data/ 

The testing script contains the following command-line arguments:
* --model_path (str): Path to the trained model file. Default is cnn_selected.keras.

* --data_path (str): Path to the test dataset file which must be in json format. Default is /data/test_data.json.

* --n (int): Number of prediction rows to print to the console. Default is 10.

* --output_filename (str): File name for the output predictions. This will save the results to the specified file in the /output directory. Default is predictions.csv.

2. Run:
```bash
python3 test.py --model_path /path/to/model --data_path /path/to/data --n 5 --output_filename model_output_datetime.csv
```

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
* ``scored``: The probability that a given site is modified

# Citing
If you use this model in your research, please cite 

# License
License information.