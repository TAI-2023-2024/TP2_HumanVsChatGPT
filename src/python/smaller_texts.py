import os, random

random.seed(24)

texts_original = []

ai_texts = 0
human_texts = 0

while ai_texts < 10 or human_texts < 10:
    filename = random.choice(os.listdir(".\\example\\AI_Human_Dataset\\test"))
    if ('ai' in filename) and ai_texts < 10:
        ai_texts += 1
        texts_original.append(filename)
    if ('human' in filename) and human_texts < 10:
        human_texts += 1
        texts_original.append(filename)

texts_original.sort()
texts_original.sort(key=len)

for item in texts_original:
    print(item)

for filename in texts_original:
    file = open('.\\example\\AI_Human_Dataset\\test\\' + filename, 'r', errors='ignore')
    text = file.readline()
    file.close()
    text_len = len(text)
    smaller_filename_50 = '.\\example\\AI_Human_Dataset\\smaller_test\\50_' + filename
    smaller_filename_25 = '.\\example\\AI_Human_Dataset\\smaller_test\\25_' + filename
    with open(smaller_filename_50, 'w',errors='ignore') as file50:
        file50.write(text[0:int(text_len/2)])
    with open(smaller_filename_25, 'w',errors='ignore') as file25:
        file25.write(text[0:int(text_len/4)])

    