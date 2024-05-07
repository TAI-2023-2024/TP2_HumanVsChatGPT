@echo off
cd C:\Users\admin\Desktop\UA\TAI\TP2_HumanVsChatGPT

(for %%k in (2 4 6 8) do (
    for %%f in (002 004 006 008 010) do (
        .\bin\fcm.exe -f .\example\AI_Human_Dataset\train\ai_train_%%f.txt -k %%k -t A
        .\bin\fcm.exe -f .\example\AI_Human_Dataset\train\human_train_%%f.txt -k %%k -t H
    )
))