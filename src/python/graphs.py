import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# plt.rcParams['axes.facecolor'] = '#ADD8E6'

results = {}

# kList = ["2","4","6","8"]
# aList = ["1","10","100"]
# dataList = ["002","004","006","008","010"]

kList = ["2","4"]
aList = ["1","10","100"]
dataList = ["002","004","006","008","010"]

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
                        counter = -1
                    counter = counter + 1

# for dic in results:
#     print(str(dic) + " : " + str(results[dic]))

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

## Organized by K

# k2 = []
# k4 = []
# k6 = []
# k8 = []

# for dic in accuracy:
#     if dic["K"] == "2":
#         k2.append(dic)
#     if dic["K"] == "4":
#         k4.append(dic)
#     if dic["K"] == "6":
#         k6.append(dic)
#     if dic["K"] == "8":
#         k8.append(dic)

# d2 = pd.DataFrame.from_dict(k2)
# d4 = pd.DataFrame.from_dict(k4)
# d6 = pd.DataFrame.from_dict(k6)
# d8 = pd.DataFrame.from_dict(k8)

## By Dataset

# d002 = []
# d004 = []
# d006 = []
# d008 = []
# d010 = []

# for dic in accuracy:
#     if dic["Dataset"] == "002":
#         d002.append(dic)
#     if dic["Dataset"] == "004":
#         d004.append(dic)
#     if dic["Dataset"] == "006":
#         d006.append(dic)
#     if dic["Dataset"] == "008":
#         d008.append(dic)
#     if dic["Dataset"] == "010":
#         d010.append(dic)

# d2 = pd.DataFrame.from_dict(d002)
# d4 = pd.DataFrame.from_dict(d004)
# d6 = pd.DataFrame.from_dict(d006)
# d8 = pd.DataFrame.from_dict(d008)
# d10 = pd.DataFrame.from_dict(d010)

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

d1 = pd.DataFrame.from_dict(a1)
d10 = pd.DataFrame.from_dict(a10)
d100 = pd.DataFrame.from_dict(a100)

plt.figure(figsize=(16, 5))

plt.subplot(131)
p1 = sns.lineplot(x='Dataset', y='Total',hue='K',data=d1,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('Alpha = 1')

plt.subplot(132)
p10 = sns.lineplot(x='Dataset', y='Total',hue='K',data=d10,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('Alpha = 10')

plt.subplot(133)
p100 = sns.lineplot(x='Dataset', y='Total',hue='K',data=d100,linestyle='-', marker='o', markersize=10)
plt.xlabel('Dataset')
plt.ylabel('Accuracy (%)')
plt.title('Alpha = 100')

plt.show()

# x = np.random.uniform(3,1,100)
# y = x * 10 + np.random.normal(3,2,100)

# data = {'x': x,
#         'y': y,
#         }
# df = pd.DataFrame(data)

# plt.figure(figsize=(8, 6)) # Width and Height of the chart
# sns.lineplot(x='x',
#              y='y',
#              data=df,
#              marker='o', # Style used to mark the join between 2 points
#             )
# plt.xlabel('X-axis') # x-axis name
# plt.ylabel('Y-axis') # y-axis name
# plt.title('Simple Connected Scatter Plot') # Add a title
# plt.show() # Display the graph