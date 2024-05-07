// Fcm.cpp : Defines the entry point for the application.
//
#include <iostream>
#include <sstream>
#include <fstream>
#include <unordered_map>
#include <math.h>

using namespace std;

unordered_map<string, unordered_map<char, int>> humanModel;
unordered_map<string, unordered_map<char, int>> chatGPTModel;

string humanTextFilename = "none";
string chatGPTTextFilename = "none";
string targetTextFilename = "none";

double alpha = 1;
double k = 2;

unordered_map<string, string> inputflags;

unordered_map<string, string> getFlags(int argc, char* argv[]) {
    unordered_map<string, string> flags;
    for (int i = 1; i < argc; ++i) {
        string arg = argv[i];
        if (arg.substr(0, 2) == "--") {
            string flag = arg.substr(2);
            if (i + 1 < argc && argv[i + 1][0] != '-') {
                flags[flag] = argv[++i];
            }
            else {
                flags[flag] = "";
            }
        }
        else if (arg.substr(0, 1) == "-") {
            string flag = arg.substr(1);
            if (i + 1 < argc && argv[i + 1][0] != '-') {
                flags[flag] = argv[++i];
            }
            else {
                flags[flag] = "";
            }
        }
    }
    return flags;
}

string cleanUpLine(string line){
    size_t last_non_whitespace = line.find_last_not_of("\r\n");
    if (last_non_whitespace != std::string::npos) {
        line = line.substr(0, last_non_whitespace + 1);
    }
    return line;
}

unordered_map<string, unordered_map<char, int>> getModel(string filename, string modelType, int k) {

    unordered_map<string, unordered_map<char, int>> map;

    map.clear();

    ifstream file(filename);

    if (!file.is_open())
    {
        std::cout << "Error opening file: " << filename << endl;
        return map;
    }

    string line = "";

    string fileModelType;
    double fileK;

    getline(file, line);
    fileModelType = cleanUpLine(line);
    getline(file, line);
    fileK = stof(line);

    if (modelType != fileModelType) {
        std::cout << "This file is does not have the expected model type " << modelType << ". File model type :  " << fileModelType << endl;
        return map;
    }

    if (k != fileK) {
        std::cout << "This file is not of the expected k " << to_string(k) << ". File k : " << to_string(fileK) << endl;
        return map;
    }

    size_t mapSize;
    getline(file, line);
    std::stringstream sstream(line);
    sstream >> mapSize;

    for (size_t i = 0; i < mapSize; ++i) {
        string outerKey;
        getline(file, outerKey);
        outerKey = cleanUpLine(outerKey);

        size_t innerMapSize;
        getline(file, line);
        std::stringstream sstream(line);
        sstream >> innerMapSize;

        unordered_map<char, int> innerMap;

        for (size_t j = 0; j < innerMapSize; ++j) {
            string innerKey;
            getline(file, innerKey);
            innerKey = cleanUpLine(innerKey);

            if (outerKey.find_first_not_of(' ') == string::npos) {
                innerKey = " ";
            }

            int innerValue;

            getline(file, line);
            innerValue = stoi(line);

            innerMap[innerKey[0]] = innerValue;
        }

        map[outerKey] = innerMap;

    }

    file.close();

    //// Print the contents of the map
    //std::cout << "Map contents:" <<endl;
    //for (const auto& pair : map) {
    //    std::cout << "Outer Key: " << pair.first << endl;
    //    std::cout << "Inner Map:" << endl;
    //    for (const auto& innerPair : pair.second) {
    //        std::cout << innerPair.first << ": " << innerPair.second << endl;
    //    }
    //    std::cout << endl;
    //}

    return map;
}

int getTotalCounts(unordered_map<char, int> map) {
    int counter = 0;
    for (const auto& pair : map) {
        counter += pair.second;
    }
    return counter;
}

int main(int argc, char* argv[])
{
    inputflags = getFlags(argc, argv);
    if (inputflags.count("h")) {
        humanTextFilename = inputflags.at("h");
    }
    else {
        std::cout << "No human text filename given" << endl;
        return 1;
    }

    if (inputflags.count("c")) {
        chatGPTTextFilename = inputflags.at("c");
    }
    else {
        std::cout << "No human text filename given" << endl;
        return 1;
    }

    if (inputflags.count("t")) {
        targetTextFilename = inputflags.at("t");
    }
    else {
        std::cout << "No human text filename given" << endl;
        return 1;
    }

    if (inputflags.count("a")) {
        alpha = stof(inputflags.at("a"));
    }
    else {
        std::cout << "No alpha given" << endl;
        return 1;
    }

    if (inputflags.count("k")) {
        k = stof(inputflags.at("k"));
    }
    else {
        std::cout << "No k given" << endl;
        return 1;
    }

    std::cout << "-> Human Text Filename: " << humanTextFilename << endl;
    std::cout << "-> ChatGPT Text Filename: " << chatGPTTextFilename << endl;
    std::cout << "-> Target Text Filename: " << targetTextFilename << endl;
    std::cout << "-> Alpha: " << to_string(alpha) << endl;
    std::cout << "-> K: " << to_string(k) << endl;

    chatGPTModel = getModel(chatGPTTextFilename, "A", k);
    humanModel = getModel(humanTextFilename, "H", k);

    ifstream file(targetTextFilename);

    if (!file.is_open())
    {
        std::cout << "Error opening file: " << targetTextFilename << endl;
        return 1;
    }

    double humanModelInfo = 0;
    double chatGPTModelInfo = 0;

    int humanModelSymbolCount = 0;
    int chatGPTModelSymbolCount = 0;

    int humanModelTotalSymbolCount = 0;
    int chatGPTModelTotalSymbolCount = 0;

    double probability = 0;
    double bits = 0;
    char letter;
    string window = "";

    while (file.get(letter)) {
        if (letter == '\n' || letter == '\t') {
            continue;
        }

        if (window.size() == k) {

            chatGPTModelSymbolCount = chatGPTModel[window][letter];
            chatGPTModelTotalSymbolCount = getTotalCounts(chatGPTModel[window]);

            probability = (double)(chatGPTModelSymbolCount + alpha) / (double)(chatGPTModelTotalSymbolCount + alpha * k);

            chatGPTModelInfo += -log2(probability);

            humanModelSymbolCount = humanModel[window][letter];
            humanModelTotalSymbolCount = getTotalCounts(humanModel[window]);

            probability = (double)(humanModelSymbolCount + alpha) / (double)(humanModelTotalSymbolCount + alpha * k);

            humanModelInfo += -log2(probability);

        }

        if (window.length() == k) {
            window.erase(0, 1);
        }

        window += letter;
    }

    std::cout << "Human Model Info: " << to_string(humanModelInfo) << endl;
    std::cout << "ChatGPT Model Info: " << to_string(chatGPTModelInfo) << endl;

    string targetType = "";

    if (humanModelInfo < chatGPTModelInfo) {
        targetType = "Human";
    }
    else if (humanModelInfo > chatGPTModelInfo) {
        targetType = "ChatGPT";
    }
    else {
        targetType = "Unknown";
    }

    std::cout << "Target Text Type : " << targetType << endl;

    return 0;
}
