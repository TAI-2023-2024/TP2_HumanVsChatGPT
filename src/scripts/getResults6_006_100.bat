@echo off
cd C:\Users\admin\Desktop\UA\TAI\TP2_HumanVsChatGPT

(for %%k in (6) do (
    (for %%f in (006) do (
        (for %%a in (100) do (
            echo K %%k A %%a F %%f
            (for %%i in (.\example\AI_Human_Dataset\test\*) do (
                echo Testing
                echo %%~nxi >> results\results_K_%%k_A_%%a_Data_%%f.txt
                .\bin\was_chatted.exe -h .\example\AI_Human_Dataset\train\ModelType_H_K_%%k_human_train_%%f.txt -c .\example\AI_Human_Dataset\train\ModelType_A_K_%%k_ai_train_%%f.txt -t %%i -k %%k -a %%a >> results\results_K_%%k_A_%%a_Data_%%f.txt
            ))
        ))
    ))
))

(for %%k in (8) do (
    (for %%f in (002) do (
        (for %%a in (1) do (
            echo K %%k A %%a F %%f
            (for %%i in (.\example\AI_Human_Dataset\test\*) do (
                echo Testing
                echo %%~nxi >> results\results_K_%%k_A_%%a_Data_%%f.txt
                .\bin\was_chatted.exe -h .\example\AI_Human_Dataset\train\ModelType_H_K_%%k_human_train_%%f.txt -c .\example\AI_Human_Dataset\train\ModelType_A_K_%%k_ai_train_%%f.txt -t %%i -k %%k -a %%a >> results\results_K_%%k_A_%%a_Data_%%f.txt
            ))
        ))
    ))
))

(for %%k in (8) do (
    (for %%f in (010) do (
        (for %%a in (10) do (
            echo K %%k A %%a F %%f
            (for %%i in (.\example\AI_Human_Dataset\test\*) do (
                echo Testing
                echo %%~nxi >> results\results_K_%%k_A_%%a_Data_%%f.txt
                .\bin\was_chatted.exe -h .\example\AI_Human_Dataset\train\ModelType_H_K_%%k_human_train_%%f.txt -c .\example\AI_Human_Dataset\train\ModelType_A_K_%%k_ai_train_%%f.txt -t %%i -k %%k -a %%a >> results\results_K_%%k_A_%%a_Data_%%f.txt
            ))
        ))
    ))
))