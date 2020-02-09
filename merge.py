import glob

read_files = glob.glob("*.json")
with open("merged_file.json", "wb") as outfile:
    outfile.write('[{}]'.format(
        ','.join([open(f, "rb").read() for f in read_files])))