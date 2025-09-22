[![](https://zenodo.org/badge/DOI/10.5281/zenodo.15980462.svg)](https://doi.org/10.5281/zenodo.15980462)

# Supplementary Material - Machine Learning Models for Indoor Positioning Using Bluetooth RSSI and Video Data: A Case Study

This repository provides supplementary material to "_Machine Learning Models for Indoor Positioning Using Bluetooth RSSI and Video Data: A Case Study_", 
a paper draft by  Tomás Mamede, Nuno Silva, [Eduardo R. B. Marques](https://www.dcc.fc.up.pt/~edrdo), [Luís M. B. Lopes](https://www.dcc.fc.up.pt/~lblopes) from [CRACS / INESC-TEC](https://www.inesctec.pt/en/centres/cracs) and [DCC/FCUP](https://www.dcc.fc.up.pt).

## Notebooks

### BRSSI models

File  | Description
------|------------
[`BRSSI_Datasets.ipynb`](BRSSI_Datasets.ipynb) | Definition of base BRSSI datasets from raw data.
[`BRSSI_WalkDatasets.ipynb`](BRSSI_WalkDatasets.ipynb) | Definition of BRSSI walk datasets from raw data.
[`BRSSI_Train.ipynb`](BRSSI_Train.ipynb) | Derivation of BRSSI models.
[`BRSSI_Eval.ipynb`](BRSSI_Eval.ipynb) | Evaluation of BRSSI models.

### CNN models

File  | Description
------|------------
[`CNN_Datasets.ipynb`](CNN_Datasets.ipynb) | Definition of base CNN datasets from raw data.
[`CNN_WalkDatasets.ipynb`](CNN_WalkDatasets.ipynb) | Definition of CNN walk datasets from raw data.
[`CNN_Train.ipynb`](CNN_Train.ipynb) | Derivation of CNN models.
[`CNN_Eval.ipynb`](CNN_Eval.ipynb) | Evaluation of CNN models.

### Hybrid models

File  | Description
------|------------
[`HM_SoftVoting.ipynb`](HM_SoftVoting.ipynb) | Soft voting model.
[`HM_Stacking.ipynb`](HM_Stacking.ipynb) | Stacking models.
[`HM_Eval.ipynb`](HM_Eval.ipynb) | Evaluation of hybrid models.
[`HM_SSAnalysis.ipynb`](HM_SSAnalysis.ipynb) | Hybrid models statistical significance analysis.

### Other

File  | Description
------|------------
[`ROI_Analysis.ipynb`](ROI_Analysis.ipynb) | Results for ROI analysis.

## Data


Folder | Description
-------|-----------
[`raw_data`](raw_data/) | Raw data acquired.
[`datasets`](datasets/) | Datasets used for training and testing.
[`results`](results/) | Result files.


