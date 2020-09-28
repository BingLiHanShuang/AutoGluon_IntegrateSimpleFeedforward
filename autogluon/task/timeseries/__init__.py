#from .tabular_prediction import *
#from .dataset import *
#from .predictor import * 

# Gluots Part
# Relative imports
from ._base import (
    ArtificialDataset,
    ComplexSeasonalTimeSeries,
    ConstantDataset,
    RecipeDataset,
    constant_dataset,
    default_synthetic,
)

__all__ = [
    "ArtificialDataset",
    "ConstantDataset",
    "ComplexSeasonalTimeSeries",
    "RecipeDataset",
    "constant_dataset",
    "default_synthetic",
]

# fix Sphinx issues, see https://bit.ly/2K2eptM
for item in __all__:
    if hasattr(item, "__module__"):
        setattr(item, "__module__", __name__)