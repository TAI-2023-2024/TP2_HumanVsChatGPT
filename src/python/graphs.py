import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import csv

# plt.rcParams['axes.facecolor'] = '#ADD8E6'

results = {}

small_results = {}

# kList = ["2","4","6","8"]
# aList = ["1","10","100"]
# dataList = ["002","004","006","008","010"]

kList = ["2","4"]
aList = ["1","10","100"]
dataList = ["002","004","006","008","010"]

small_results_files = ["ai_26619.txt","ai_28125.txt","ai_29587.txt","ai_43188.txt","ai_116324.txt","ai_194780.txt","ai_248497.txt","ai_267496.txt","ai_272490.txt","ai_344807.txt"
                     "human_183848.txt","human_261152.txt","human_269207.txt","human_297328.txt","human_297991.txt","human_302685.txt","human_312544.txt","human_339587.txt","human_391991.txt","human_421303.txt",]

is_small__result = False

for k in kList:
    for a in aList:
        for data in dataList:
            results[(k,a,data)] = {}
            results[(k,a,data)]["Human"] = 0
            results[(k,a,data)]["ChatGPT"] = 0
            filename = f".\\results\\results_K_{k}_A_{a}_Data_{data}.txt"
            with open(filename) as file:
                counter = 0
                type = ""
                for line in file:
                    if counter == 0:
                        if line.strip() in small_results_files:
                            small_filename = line.strip()
                            is_small__result = True
                            if (k,a,data) not in small_results.keys():
                                small_results[(k,a,data)] = {}
                        if "ai" in line:
                            type = "ChatGPT"
                        elif "human" in line:
                            type = "Human"
                        else:
                            print("Unexpected error")
                            print(filename)
                            print(line)
                            exit()
                    if counter == 8:
                        if type in line:
                            results[(k,a,data)][type] += 1
                        if is_small__result:
                            if type in line:
                                small_results[(k,a,data)][small_filename] = 1
                            else:
                                small_results[(k,a,data)][small_filename] = 0
                            is_small__result = False
                        counter = 0
                        continue
                    counter = counter + 1

            # s_filename = f".\\results\\smaller_results_K_{k}_A_{a}_Data_{data}.txt"
            # with open(s_filename) as file:
            #     counter = 0
            #     for line in file:
            #         if counter == 0:
            #             small_filename = line.strip()
            #             if small_filename not in small_results.keys():
            #                 small_results[small_filename] = {}
            #             if "ai" in line:
            #                 type = "ChatGPT"
            #             elif "human" in line:
            #                 type = "Human"
            #         if counter == 8:
            #             if type in line:
            #                 small_results[small_filename][(k,a,data)] = 1
            #             else:
            #                 small_results[small_filename][(k,a,data)] = 0
            #             is_small__result = False
            #             counter = 0
            #             continue
            #         counter = counter + 1

# for tuple in small_results:
#     print(str(tuple) +  " -> " + str(small_results[tuple]))
#     # for small_filename in small_results[tuple]:
#     #     # if small_results[tuple][small_filename] == 0:
#     #     #     print(str(tuple) +  " -> " + str(small_filename) + " : " + str(small_results[tuple][small_filename]))
#     #     print(str(tuple) +  " -> " + str(small_results[tuple]))


accuracy = []
             
for k in kList:
    for a in aList:
        for data in dataList:
            accuracy.append({"K" : k, "Alpha" : a, "Dataset" : data, "Human" : 0, "ChatGPT" : 0, "Total" : 0})


# for dic in accuracy:
#     print(str(dic))

#ADD

counter = 0

for k in kList:
    for a in aList:
        for data in dataList:
            
            #Add
            human_hits = results[(k,a,data)]["Human"]
            ai_hits = results[(k,a,data)]["ChatGPT"]
            total_hits = human_hits + ai_hits

            accuracy[counter]["Human"] += human_hits
            accuracy[counter]["ChatGPT"] += ai_hits
            accuracy[counter]["Total"] += total_hits
            counter += 1

#DIVIDE
counter = 0

for k in kList:
    for a in aList:
        for data in dataList:
            accuracy[counter]["Human"] = accuracy[counter]["Human"] / (500)
            accuracy[counter]["ChatGPT"] = accuracy[counter]["ChatGPT"] / (500)
            accuracy[counter]["Total"] = accuracy[counter]["Total"] / (500 * 2)
            counter += 1

keys = accuracy[0].keys()

with open(".\\results\\aggregated_results_and_graphs\\accuracy.csv",'w', newline='') as csv_file:
    dict_writer = csv.DictWriter(csv_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(accuracy)


## Organized by K

k2 = []
k4 = []
k6 = []
k8 = []

for dic in accuracy:
    if dic["K"] == "2":
        k2.append(dic)
    if dic["K"] == "4":
        k4.append(dic)
    if dic["K"] == "6":
        k6.append(dic)
    if dic["K"] == "8":
        k8.append(dic)

d_k2 = pd.DataFrame.from_dict(k2)
d_k4 = pd.DataFrame.from_dict(k4)
d_k6 = pd.DataFrame.from_dict(k6)
d_k8 = pd.DataFrame.from_dict(k8)

## By Dataset

d002 = []
d004 = []
d006 = []
d008 = []
d010 = []

for dic in accuracy:
    if dic["Dataset"] == "002":
        d002.append(dic)
    if dic["Dataset"] == "004":
        d004.append(dic)
    if dic["Dataset"] == "006":
        d006.append(dic)
    if dic["Dataset"] == "008":
        d008.append(dic)
    if dic["Dataset"] == "010":
        d010.append(dic)

d_d002 = pd.DataFrame.from_dict(d002)
d_d004 = pd.DataFrame.from_dict(d004)
d_d006 = pd.DataFrame.from_dict(d006)
d_d008 = pd.DataFrame.from_dict(d008)
d_d010 = pd.DataFrame.from_dict(d010)

## By Alpha

a1 = []
a10 = []
a100 = []

for dic in accuracy:
    if dic["Alpha"] == "1":
        a1.append(dic)
    if dic["Alpha"] == "10":
        a10.append(dic)
    if dic["Alpha"] == "100":
        a100.append(dic)

d_a1 = pd.DataFrame.from_dict(a1)
d_a10 = pd.DataFrame.from_dict(a10)
d_a100 = pd.DataFrame.from_dict(a100)

plt.figure(1,figsize=(20,10))

plt.subplot(131)
p1 = sns.lineplot(x='Dataset', y='Total',hue='K',data=d_a1,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('Alpha = 1')

plt.subplot(132)
p10 = sns.lineplot(x='Dataset', y='Total',hue='K',data=d_a10,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('Alpha = 10')

plt.subplot(133)
p100 = sns.lineplot(x='Dataset', y='Total',hue='K',data=d_a100,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('Alpha = 100')

plt.savefig('.\\results\\aggregated_results_and_graphs\\alpha.png')

plt.figure(2,figsize=(20,10))

plt.subplot(321)
p1 = sns.lineplot(x='K', y='Total',hue='Alpha',data=d_d002,linestyle='-', marker='o', markersize=10)
plt.xlabel('K')
plt.ylabel('Accuracy (%)')
plt.title('Dataset 002')

plt.subplot(322)
p10 = sns.lineplot(x='K', y='Total',hue='Alpha',data=d_d004,linestyle='-', marker='o', markersize=10)
plt.xlabel('K')
plt.ylabel('Accuracy (%)')
plt.title('Dataset 004')

plt.subplot(323)
p100 = sns.lineplot(x='K', y='Total',hue='Alpha',data=d_d006,linestyle='-', marker='o', markersize=10)
plt.xlabel('K')
plt.ylabel('Accuracy (%)')
plt.title('Dataset 006')

plt.subplot(324)
p100 = sns.lineplot(x='K', y='Total',hue='Alpha',data=d_d008,linestyle='-', marker='o', markersize=10)
plt.xlabel('K')
plt.ylabel('Accuracy (%)')
plt.title('Dataset 008')

plt.subplot(325)
p100 = sns.lineplot(x='K', y='Total',hue='Alpha',data=d_d010,linestyle='-', marker='o', markersize=10)
plt.xlabel('K')
plt.ylabel('Accuracy (%)')
plt.title('Dataset 010')

plt.savefig('.\\results\\aggregated_results_and_graphs\\dataset.png')

plt.figure(3,figsize=(20,10))

plt.subplot(221)
p1 = sns.lineplot(x='Dataset', y='Total',hue='Alpha',data=d_k2,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('K 2')

plt.subplot(222)
p10 = sns.lineplot(x='Dataset', y='Total',hue='Alpha',data=d_k4,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('K 4')

# plt.subplot(223)
# p100 = sns.lineplot(x='Dataset', y='Total',hue='Alpha',data=d_k6,linestyle='-', marker='o', markersize=10)
# plt.xlabel('Dataset')
# plt.ylabel('Accuracy (%)')
# plt.title('K 6')

# plt.subplot(224)
# p100 = sns.lineplot(x='Dataset', y='Total',hue='Alpha',data=d_k8,linestyle='-', marker='o', markersize=10)
# plt.xlabel('Dataset')
# plt.ylabel('Accuracy (%)')
# plt.title('K 8')

plt.savefig('.\\results\\aggregated_results_and_graphs\\k.png')


# plt.show()


