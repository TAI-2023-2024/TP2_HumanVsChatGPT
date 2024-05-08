# TP2_HumanVsChatGPT
Repository for Lab Work 2 for TAI

## Dataset

Dataset for both Human Text and Text rewritten by ChatGPT obtained from: https://www.kaggle.com/code/syedali110/ai-generated-vs-human-text-95-accuracy/input

## How to compile

```bash
g++ -o bin/fcm src/fcm.cpp
g++ -o bin/was_chatted src/was_chatted.cpp
```

## How to run

### FCM

Below are the parameters to run fcm.
All parameters are optional except the parameter f.

```bash
./bin/fcm -k <order> -t <model type> -f <path to file>
```
- parameter k: Order of the finite-context model; default value is 2
- parameter t: Model Type (Either H for Human or A for AI/ChatGPT); default value is H
- parameter f: Path to the file with the texts to create the model from

Example:

```bash
./bin/fcm -k 4 -t A -f example/AI_Human_Dataset/train/ai_train_002.txt
```

### Was Chatted

Below are the parameters to run was_chatted.
The 

```bash
./bin/was_chatted -h <path to file with human model> -c <path to file with chatgpt model> -t <path to file with target text> -k <order> -a <alpha>
```
- parameter h: Path to the file with the human model
- parameter c: Path to the file with the ChatGPT model
- parameter t: Path to the file with the target text
- parameter k: Order of the finite-context model; default value is 2
- parameter a: Alpha (smoothing parameter); default value is 1

Example:

```bash
./bin/was_chatted -h  example/AI_Human_Dataset/train/ModelType_H_K_4_human_train_002.txt -c example/AI_Human_Dataset/train/ModelType_A_K_4_ai_train_002.txt -t example/AI_Human_Dataset/test/ai_1913.txt -k 4 -a 10
```

## Large File Problems

Some files in our repository are very large, which lead to the need to use Git Large File System (GLSF) which means that if the quota is reached, some files may not be correctly downloaded when cloaning the repository.

For this reason, a new repository was created without the original dataset file so it does not consume a lot of credit when cloning. This repo is available at https://github.com/goncalo-machado/TAI-2-Assignment

If for some reason it is not possible to clone, we compressed the full repo which is downloadable from the following link : https://drive.google.com/file/d/1eQikfBlcP07T84sCU43gkWv4l9A1XcAO/view?usp=sharing
