"""Summary
"""
import warnings
warnings.filterwarnings("ignore")
import sys

from ..utils import print_sys
from . import bi_pred_dataset, multi_pred_dataset
from ..metadata import dataset_names

class DTI(bi_pred_dataset.DataLoader):

    """Drug-Target Interaction Prediction

    Regression task. Given the target amino acid sequence/compound SMILES string, predict their binding affinity.

    
    Attributes:
        entity1_name (str): Description
        entity2_name (str): Description
        two_types (bool): Description
    """
    
    def __init__(self, name, path='./data', label_name=None,
                 print_stats=False):
        """Summary
        
        Args:
            name (TYPE): Description
            path (str, optional): Description
            label_name (None, optional): Description
            print_stats (bool, optional): Description
        """
        super().__init__(name, path, label_name, print_stats,
                         dataset_names=dataset_names["DTI"])
        self.entity1_name = 'Drug'
        self.entity2_name = 'Target'
        self.two_types = True

        if print_stats:
            self.print_stats()

        print('Done!', flush=True, file=sys.stderr)