# Data folder

Place the In–Ga–Sn–Zn resistivity dataset used in the paper into this folder.

The main script looks for an Excel file with the same structure as the original experimental sheet, for example:

- `data/手动计算物理特征new.xlsx`
- or `data/resistivity_dataset.xlsx`

The file should contain:

- Target resistivity (mΩ·cm).
- Process variables: sintering temperature (℃), holding time (h).
- Elemental fractions: In, Ga, Sn, Zn.
- Physics descriptors: VEC, ΔVEC, Tm, ΔTm, r, Δr, χ, Δχ (if available).

The loader in `physics_guided_ml_for_resistivity.py` will automatically:

1. Drop fully empty rows/columns.
2. Detect the header row.
3. Coerce numeric columns and remove rows with non-finite targets.

> **Note:** The dataset itself is not included in this repository. Please use your own copy consistent with the manuscript.
