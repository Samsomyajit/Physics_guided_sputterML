# Geometry-Aware & Calibrated ML for Resistivity
```
Authors: Nuo Cheng a, Somyajit Chakraborty b, Xiaokai Liu a, Wenyu Zhang a, Xina Liang a, Hetao Zhao a, Wenhui Bi a, Mingzhen Zhang a, Yang Liu a,d,c* , Benshuang Sun a,c,d, Jilin He a,c,d
a School of Materials Science and Engineering, Zhengzhou University, Zhengzhou 450001, China
b School of Chemical Engineering, Shanghai Jiao Tong University, Shanghai 200240, China
c Zhongyuan Critical Metals Laboratory, Zhengzhou, 450001, China
d The National Key Laboratory of Special Rare Metal Materials, Zhengzhou University, 450001, China
```
This repository provides a reproducible Python implementation of the machine-learning workflow described in:

> Geometry-Aware and Calibrated Uncertainty Learning for Designing Indium Oxide-Based Alternative Sputtering Targets

![](https://github.com/Samsomyajit/Physics_guided_sputterML/blob/main/data/FlowSputRes.png)

The code implements a **physics-guided small-data pipeline** for predicting and optimizing the resistivity of In–Ga–Sn–Zn oxide sputtering targets from composition, process variables, and physics descriptors. It follows the same stages as the paper:

1. Robust Excel ingestion and cleaning for the 86-sample dataset.
2. Physics-guided feature construction (electronic/size mismatch descriptors, compositional complexity).
3. Leakage-safe nested cross-validation with gradient-boosted tree models (XGBoost, LightGBM, CatBoost).
4. Global feature attribution with SHAP.
5. Monotone isotonic calibration and uncertainty quantification.
6. PSO-based inverse design of new compositions and process conditions.
7. Figure and table generation matching the main text and supplementary information.

## Repository layout

```text
physics-guided-ml-resistivity/
├── README.md                  # This file
├── LICENSE                    # MIT license (feel free to change)
├── requirements.txt           # Python dependencies
├── src/
│   └── physics_guided_ml_for_resistivity.py  # Main end-to-end pipeline
├── scripts/
│   └── run_full_pipeline.py   # Thin wrapper to run the full workflow
└── data/
    └── README.md              # Where to put the Excel dataset
```

### `src/physics_guided_ml_for_resistivity.py`

This is an export of the original Colab notebook. When executed, it will:

1. Load the resistivity dataset from one of the paths listed in `CANDIDATE_PATHS`.
2. Automatically detect the header row and key columns (target, sintering temperature, holding time, composition, physics descriptors).
3. Build engineered features and run the nested CV protocol.
4. Fit XGBoost / LightGBM / CatBoost models and the stacked ensemble.
5. Apply isotonic calibration and compute out-of-fold metrics.
6. Run PSO-based inverse design and export the top candidates.
7. Write all intermediate tables and final figures into an `out/` directory (created next to the script if missing).

The script is intentionally self-contained and can be run both in a notebook and as a standalone Python program.

### Dataset placement

The script expects the experimental dataset as an Excel file with the same structure used in the paper (86 valid rows after cleaning). For convenience, we use the following default relative paths:

```python
CANDIDATE_PATHS = [
    "data/手动计算物理特征new.xlsx",
    "data/resistivity_dataset.xlsx",
]
```

Place your dataset at one of these locations (or edit `CANDIDATE_PATHS` at the top of the script to match your filename).

> **Important:** If the dataset is not found at any of the candidate paths, the script will try to fall back to a Colab-style upload. In a non-Colab environment this will fail, so make sure the Excel file exists in `data/` before you run anything.

### Output

By default, results are written into an `out/` folder next to the script, including:

- Cleaned dataset snapshots used for modeling.
- SHAP summary plots and dependence plots.
- Correlation and PCA loading maps.
- Nested CV metrics and per-fold summaries.
- Calibration and parity plots.
- PSO-optimized composition/process candidates and their predicted resistivity.

These correspond to the tables and figures in the manuscript (main text and supplementary).

## Installation

We recommend using a fresh virtual environment (conda or venv):

```bash
# Clone your GitHub fork
git clone https://github.com/your-username/physics-guided-ml-resistivity.git
cd physics-guided-ml-resistivity

# (Optional) create a conda env
conda create -n resistivity-ml python=3.10
conda activate resistivity-ml

# Install dependencies
pip install -r requirements.txt
```

Most experiments in the paper were run with Python 3.10; newer versions should also work, but if you hit compatibility issues, try 3.10 or 3.11 first.

## Running the full pipeline

Once dependencies are installed and the Excel dataset is in `data/`, you can reproduce the main results with:

```bash
python scripts/run_full_pipeline.py
```

This wrapper simply imports the main script and executes it, so you can also run:

```bash
python src/physics_guided_ml_for_resistivity.py
```

to get identical behavior.

Depending on your CPU/GPU and Optuna settings, a full run (including hyperparameter search and PSO) can be computationally intensive. You can shorten it for quick tests by editing the Optuna/trial counts and PSO settings near the bottom of the script.

## Using this codebase for your own work

Although this repository is tuned to the specific IGTO/IGZO/IZTO dataset in the paper, most of the pipeline components are generic:

- The smart Excel loader and robust header detection.
- Physics-style feature engineering and leak-safe preprocessing.
- Nested CV, calibration, and uncertainty quantification.
- PSO-based inverse design with simplex projection and process constraints.

You can adapt them to other small-data materials design problems by:

1. Replacing the Excel dataset and updating `CANDIDATE_PATHS`.
2. Adjusting the feature-engineering section to your own descriptors.
3. Modifying the PSO bounds and constraints to match your composition/process space.

## License

This project is released under the MIT License (see `LICENSE`). If you prefer a different license for the GitHub repository, you can replace the file before pushing.
