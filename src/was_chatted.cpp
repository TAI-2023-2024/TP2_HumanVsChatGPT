// Fcm.cpp : Defines the entry point for the application.
//
#include <iostream>
#include <sstream>
#include <fstream>
#include <unordered_map>

using namespace std;

unordered_map<string, unordered_map<char, int>> markv_freq;

string inputFilename = "none";   // File name

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

int main(int argc, char* argv[])
{

    // get input paramenters
    inputflags = getFlags(argc, argv);
    if (inputflags.count("f")) {
        inputFilename = inputflags.at("f");
    }
    else {
        std::cout << "No filename given\n";
        return 1;
    }

    std::cout << "-> File: " << inputFilename << endl;

    ifstream file(inputFilename);

    if (!file.is_open())
    {
        std::cout << "FCM: Error opening file: " << inputFilename;
        return 1;
    }

    string line = "";

    string modelType;
    int k;

    getline(file, modelType);

    getline(file, line);
    k = stoi(line);

    size_t mapSize;
    getline(file, line);
    std::stringstream sstream(line);
    sstream >> mapSize;

    for (size_t i = 0; i < mapSize; ++i) {
        // Read the outer key
        string outerKey;
        getline(file, outerKey);

        // Read the size of the inner map
        size_t innerMapSize;
        getline(file, line);
        std::stringstream sstream(line);
        sstream >> innerMapSize;

        // Create the inner map
        unordered_map<char, int> innerMap;

        // Read key-value pairs of the inner map
        for (size_t j = 0; j < innerMapSize; ++j) {
            string innerKey;
            getline(file, innerKey);

            if (outerKey.find_first_not_of(' ') == string::npos) {
                innerKey = " ";
            }

            int innerValue;

            getline(file, line);
            innerValue = stoi(line);

            innerMap[innerKey[0]] = innerValue;
        }

        // Insert the inner map into the outer map
        markv_freq[outerKey] = innerMap;

    }

    // Close the file
    file.close();

    // Print the values of the two variables
    std::cout << "Model Type: " << modelType << endl;
    std::cout << "k: " << k << endl;
    std::cout << "Size of map: " << markv_freq.size() << endl;

    //// Print the contents of the map
    //std::cout << "Map contents:" <<endl;
    //for (const auto& pair : markv_freq) {
    //    std::cout << "Outer Key: " << pair.first << endl;
    //    std::cout << "Inner Map:" << endl;
    //    for (const auto& innerPair : pair.second) {
    //        std::cout << innerPair.first << ": " << innerPair.second << endl;
    //    }
    //    std::cout << endl;
    //}

    return 0;
}
