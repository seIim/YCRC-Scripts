import os
import pandas as pd 
from rspLib import *

# arraysize = int(os.environ['SLURM_ARRAY_TASK_COUNT'])
# thisrank = int(os.environ['SLURM_ARRAY_TASK_ID'])
arraysize = 10
thisrank = 0

df = pd.read_csv('Grid/Input.dat', sep='\s+')

df = df[ df['model'] % arraysize == thisrank]

os.chdir(f'Work/{thisrank}')

controls = f'../inlists/controls_{thisrank}'

for i in range(len(df)):

	lines = getInlist(controls)

	updateKey(lines, 'RSP_max_num_periods', 1)

	updateInlist(df, controls, lines, i)

	os.system('./mk')
	os.system('./rn')
