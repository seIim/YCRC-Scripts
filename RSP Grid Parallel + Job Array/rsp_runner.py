import pandas as pd

def updateKey(lines, key, newval):

	for i, line in enumerate(lines):
		if key in line:
			lines[i] = f"\t   {key} = {newval}\n"

def getInlinst(f):

	file = open(f, "r")
	lines = file.readlines()
	file.close()

	return lines

def updateInlist(df, f, data, ind):

	for key in df.columns.values.tolist()[1:]:
		updateKey(lines, key, df[key].iloc[ind])

	updateKey(lines, "log_directory", f"\'LOGS/logs_{ind}\'")
	updateKey(lines, "photo_directory", f"\'photos/photos_{ind}\'")

	file = open(f, "w")
	file.truncate(0)
	for line in lines:
		file.write(f"{line}")
	file.close()


# df = pd.read_csv('linear_grid.dat', sep='\s+')

# for row in df['model']:
# 	updateInlist(df, "inlist_rsp_common", lines, row)

# # print(df['RSP_mass'].iloc[0])

