import os
import pandas as pd 
from rspLib import *
import sys

arraysize = int(os.environ['SLURM_ARRAY_TASK_COUNT'])
thisrank = int(os.environ['SLURM_ARRAY_TASK_ID'])
# arraysize = 10
# thisrank = 0

i = sys.argv[1]

df = pd.read_csv('Grid/Input.dat', delim_whitespace=True)

df = df[ df['model'] % arraysize == (thisrank - 1) ]

os.chdir(f'Work/{thisrank}')

controls = f'../inlists/controls_{thisrank}'

inlist = getInlist('inlist')
updateKey(inlist, 'extra_controls_inlist_name(1)', f"\'../inlists/controls_{thisrank}\'")
writeAndSave('inlist', inlist)

lines = getInlist(controls)

updateKey(lines, 'max_model_number', 1)
updateKey(lines, "log_directory", f"\'../LOGS/logs_{df['model'].iloc[i]}\'")
updateKey(lines, "photo_directory", f"\'../photos/photos_{df['model'].iloc[i]}\'")

updateInlist(df, controls, lines, i)

# for i in range(len(df)):

# 	lines = getInlist(controls)

# 	updateKey(lines, 'max_model_number', 1)

# 	updateInlist(df, controls, lines, i)

# 	os.system('./mk')
# 	os.system('./rn')
