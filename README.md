# m6a-detection-project

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Interpretation](#intepretation)
- [Citing](#citing)
- [License](#license)

## Overview
This project aims to address these challenges by developing a robust machine-learning classifier for identifying m6A modifications in RNA-Seq data, specifically focusing on human cell lines from the SG-NEx Project (2021). By enhancing our ability to detect m6A modifications, we hope to contribute to a deeper understanding of m6A's role in cancer and its potential as a target for therapeutic intervention.


## Installation
To install dependencies, run
```
pip install -r requirements.txt
```

## Usage
Place test data under /data/

To run infererence:
```
python test.py
```

## Intepretation of outputs
The output file `results.csv` will be under /output/. It contains the probability of modification at each individual position for each transcript. The output file will have 3 columns

* ``transcript_id``: The transcript id of the predicted position
* ``transcript_position``: The transcript position of the predicted position
* ``scored``: The probability that a given site is modified

## Citing
If you use this model in your research, please cite 

## License
License information.