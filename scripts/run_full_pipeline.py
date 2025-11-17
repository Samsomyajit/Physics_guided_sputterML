"""Thin wrapper to run the full resistivity ML pipeline.

Usage:
    python scripts/run_full_pipeline.py

This will import and execute `src/physics_guided_ml_for_resistivity.py`,
which performs data loading, model training, calibration, PSO, and
figure/table export.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
src_dir = ROOT / "src"
if str(src_dir) not in sys.path:
    sys.path.insert(0, str(src_dir))

if __name__ == "__main__":
    # Importing the module executes the end-to-end workflow.
    import physics_guided_ml_for_resistivity  # noqa: F401
