import re
file = open("outSIFTRaw.txt",'w+')

with open("outputDup.txt") as f:
    content = f.readlines()
    for i in content:
        found = re.search(r'Ratio is (.*)', i);
        # foundRunTime= re.search(r'Training.*?:(.*)', i);
        # foundKVal = re.search(r'.*k=(.*?) and', i);
        # foundDataSet = re.search(r'.*dataset=(.*?) with', i);



        if found:
            # print("found " + found.group(1))
            file.write(found.group(1)+"\n")

file.close()