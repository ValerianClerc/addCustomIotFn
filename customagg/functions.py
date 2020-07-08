import re
import logging
import datetime as dt
import math
import numpy as np
import pandas as pd

from iotfunctions.base import BaseSimpleAggregator
from iotfunctions.ui import (UIMultiItem,UIExpression)

logger = logging.getLogger(__name__)

# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'git+https://github.com/ValerianClerc/addCustomIotFn@starter_agg_package'

class HelloWorldAggregatorVC(BaseSimpleAggregator):
    '''
    The docstring of the function will show as the function description in the UI.
    '''

    def __init__(self, input_items=None, expression=None, output=None):
        if expression is None or not isinstance(expression, str):
            raise RuntimeError("argument expression must be provided and must be a string")

        self.input_items = input_items
        self.expression = expression
        self.output = output

    def execute(self, group):
        return eval(re.sub(r"\$\{GROUP\}", r"group", self.expression))

    @classmethod
    def build_ui(cls):
        inputs = []
        inputs.append(UIMultiItem(name='input_items', datatype=None, description=('Choose the data items'
                                                                            ' that you would like to'
                                                                                  ' aggregate'),
                                  output_item='output', is_output_datatype_derived=True))

        inputs.append(UIExpression(name='expression', description='Use ${GROUP} to reference the current grain.'
                                                    'All Pandas Series methods can be used on the grain.'
                                                    'For example, ${GROUP}.max() - ${GROUP}.min().'))
        return (inputs, [])
