import pandas as pd 
  
df = pd.DataFrame(pd.read_excel(".\example\ieee-init.xlsx")) 
  
df = df.drop('id', axis=1)
df = df.drop('keyword', axis=1)
df = df.drop('title', axis=1)

with open('.\example.\human_text.txt', 'w', errors='ignore') as file:

    for index, row in df.iterrows():
        text = row['abstract']
        text = text.replace('\n', '')
        file.write(text)

df = pd.DataFrame(pd.read_excel(".\example\ieee-chatgpt-generation.xlsx")) 
  
df = df.drop('id', axis=1)
df = df.drop('keyword', axis=1)
df = df.drop('title', axis=1)

with open('.\example.\chatgpt_text.txt', 'w', errors='ignore') as file:

    for index, row in df.iterrows():
        text = row['abstract']
        text = text.replace('\n', '')
        file.write(text)
