import os
import pandas as pd 
from rspLib import *

# arraysize = int(os.environ['SLURM_ARRAY_TASK_COUNT'])
# thisrank = int(os.environ['SLURM_ARRAY_TASK_ID'])
arraysize = 50
thisrank = 0

df = pd.read_csv('linear_grid.dat', sep='\s+')

df = df[ df['model'] % arraysize == thisrank]

# print('These are the models I would run if this was real: \n')
# print(df)

os.chdir(os.environ['MESA_DIR'])
# print(os.listdir())

