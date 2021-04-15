import os

list_files = []
for root, dirs, files in os.walk("."):
	for file in files:
		list_files.append(file)
		os.rename(file, file.replace(" - xxxx.ss", ""))


for index, file in enumerate(list_files):
	rename = file.replace(" - xxxx.ss", "")
	list_files[index] = rename
