from dataclasses import fields

import filepath
import pandas as pd

data = pd.read_csv(filepath, names=fields, encoding='latin1')