
# =============================================================================
# this function receives a cmd (list of args) and returns the result as a 
# pandas dataframe

import subprocess
import pandas as pd
from io import StringIO

def execute_to_df(cmd:list,sep='\t',header=None, index_col=None) -> pd.DataFrame:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    csv = StringIO(process.stdout.read().decode())
    data = pd.read_csv(csv, header=header, index_col=index_col, sep=sep)
    csv.close()
    return data
