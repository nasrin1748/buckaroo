from buckaroo.buckaroo_widget import BuckarooWidget
from .customizations.polars_analysis import PL_Analysis_Klasses
#from buckaroo.customizations.polars_analysis import
from .pluggable_analysis_framework.polars_analysis_management import (
    PlDfStats)



class PolarsBuckarooWidget(BuckarooWidget):
    """TODO: Add docstring here
    """
    #command_classes = DefaultCommandKlsList
    analysis_classes = PL_Analysis_Klasses
    DFStatsClass = PlDfStats
