import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help=" Arff archive ")
args = vars(ap.parse_args())
dataset = args["dataset"]
dataset_split = str(dataset).split(".")
dataset_csv = dataset_split[len(dataset_split) - 2]
try:
    file_in = open(dataset, 'r')
    file_out = open(dataset[:-5]+".csv", 'w')
except:
    print("Error reading the ", dataset)
j = 0
k = 0
for i in file_in:
    if("@" in i):
        k += 1
        if("class" in i):
            classe =i.split(",") 
            qnt_classes = len(classe)
    if("%" not in i and "@" not in i):
        j += 1
qnt_amostras = (j-1)
qnt_features = k - 3
file_out.write("IND"+ ", " + "Y")
for i in range(qnt_features):
    file_out.write(", F"+str(i+1))
file_out.write("\n")
file_in = open(dataset, 'r')
j = 0
for i in file_in:
    if("%" not in i and "@" not in i):
        if (j > 0):
            txt_ = i.split(",")
            txt_num = ""
            txt_num += str(j)+", "
            classe = ""
            for l in range(len(txt_[len(txt_)-1]) - 1):
                classe += txt_[len(txt_)-1][l]
            txt_num += classe
            for k in range(len(txt_)-1):
                txt_num += "," + txt_[k] 
            file_out.write(txt_num + "\n")
        j += 1
file_out.close()
file_in.close()