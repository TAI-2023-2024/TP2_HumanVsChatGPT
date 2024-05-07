import pandas as pd

df = pd.read_csv('.\example\AI_Human_Dataset\AI_Human.csv')

grouped = df.groupby(df.generated)

df_ai = grouped.get_group(1.0)
df_human = grouped.get_group(0.0)

df_test_ai = df_ai.sample(n=500,random_state=24)
df_test_human = df_human.sample(n=500, random_state=24)

df_train_ai = df_ai.drop(df_test_ai.index)
df_train_human = df_human.drop(df_test_human.index)

print("All Dataframes ready. Starting file writing")

print("Starting - Test AI Files")

for index, row in df_test_ai.iterrows():
    filename = '.\\example\\AI_Human_Dataset\\test\\ai_' + str(index) + '.txt'
    with open(filename, 'w', errors='ignore') as file:
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)

print("Done - Test AI Files")

print("Starting - Test Human Files")

for index, row in df_test_human.iterrows():
    filename = '.\\example\\AI_Human_Dataset\\test\\human_' + str(index) + '.txt'
    with open(filename, 'w', errors='ignore') as file:
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)

print("Done - Test human files")

#10% Train Files

print("Starting - Train AI Files - 10%")

df_train_ai_010 = df_ai.sample(frac=0.1, random_state=24)
df_train_human_010 = df_human.sample(frac=0.1, random_state=24)

with open('.\\example\\AI_Human_Dataset\\train\\ai_train_010.txt', 'w', errors='ignore') as file:
    for index, row in df_train_ai_010.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)

print("Done - Train AI Files - 10%")

print("Starting - Train Human Files - 10%")

with open('.\\example\\AI_Human_Dataset\\train\\human_train_010.txt', 'w', errors='ignore') as file:
    for index, row in df_train_human_010.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)
        
print("Done - Train Human Files - 08%")

# 8% Train Files

df_train_ai_008 = df_train_ai_010.sample(frac=0.8, random_state=24)
df_train_human_008 = df_train_human_010.sample(frac=0.8, random_state=24)

with open('.\\example\\AI_Human_Dataset\\train\\ai_train_008.txt', 'w', errors='ignore') as file:
    for index, row in df_train_ai_008.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)

print("Done - Train AI Files - 08%")

print("Starting - Train Human Files - 08%")

with open('.\\example\\AI_Human_Dataset\\train\\human_train_008.txt', 'w', errors='ignore') as file:
    for index, row in df_train_human_008.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)
        
print("Done - Train Human Files - 08%")

# 8% Train Files

df_train_ai_006 = df_train_ai_008.sample(frac=0.75, random_state=24)
df_train_human_006 = df_train_human_008.sample(frac=0.75, random_state=24)

with open('.\\example\\AI_Human_Dataset\\train\\ai_train_006.txt', 'w', errors='ignore') as file:
    for index, row in df_train_ai_006.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)

print("Done - Train AI Files - 06%")

print("Starting - Train Human Files - 06%")

with open('.\\example\\AI_Human_Dataset\\train\\human_train_006.txt', 'w', errors='ignore') as file:
    for index, row in df_train_human_006.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)
        
print("Done - Train Human Files - 06%")

# 4% Train Files

df_train_ai_004 = df_train_ai_006.sample(frac=0.66, random_state=24)
df_train_human_004 = df_train_human_006.sample(frac=0.66, random_state=24)

with open('.\\example\\AI_Human_Dataset\\train\\ai_train_004.txt', 'w', errors='ignore') as file:
    for index, row in df_train_ai_004.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)

print("Done - Train AI Files - 04%")

print("Starting - Train Human Files - 04%")

with open('.\\example\\AI_Human_Dataset\\train\\human_train_004.txt', 'w', errors='ignore') as file:
    for index, row in df_train_human_004.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)
        
print("Done - Train Human Files - 04%")

# 2% Train Files

df_train_ai_002 = df_train_ai_004.sample(frac=0.5, random_state=24)
df_train_human_002 = df_train_human_004.sample(frac=0.5, random_state=24)

with open('.\\example\\AI_Human_Dataset\\train\\ai_train_002.txt', 'w', errors='ignore') as file:
    for index, row in df_train_ai_002.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)

print("Done - Train AI Files - 02%")

print("Starting - Train Human Files - 02%")

with open('.\\example\\AI_Human_Dataset\\train\\human_train_002.txt', 'w', errors='ignore') as file:
    for index, row in df_train_human_002.iterrows():
        text = row['text']
        text = text.replace('\n', '')
        text = text.replace('\'', '')
        file.write(text)
        
print("Done - Train Human Files - 02%")