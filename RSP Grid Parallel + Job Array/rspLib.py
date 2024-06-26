import pandas as pd

def updateKey(lines, key, newval):

	for i, line in enumerate(lines):
		if key in line:
			lines[i] = f"\t   {key} = {newval}\n"

def getInlist(f):

	file = open(f, "r")
	lines = file.readlines()
	file.close()

	return lines

def writeAndSave(f, lines):
	file = open(f, "w")
	file.truncate(0)
	for line in lines:
		file.write(f"{line}")
	file.close()

def updateInlist(df, f, lines, ind):

	for key in df.columns.values.tolist()[1:]:
		updateKey(lines, key, df[key].iloc[ind])

	writeAndSave(f, lines)

# df = pd.read_csv('linear_grid.dat', sep='\s+')

# for row in df['model']:
# 	updateInlist(df, "inlist_rsp_common", lines, row)

# # print(df['RSP_mass'].iloc[0])

