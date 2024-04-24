// Fcm.cpp : Defines the entry point for the application.
//
#include <iostream>
#include <sstream>
#include <fstream>
#include <unordered_map>

using namespace std;

const char separator = ',';

#pragma region subclasses
class markovf
{
private:
    string symbols;
    unordered_map<string, unordered_map<char, uint64_t>> markv_freq;

public:
    int Increment(string seq, char a)
    {
        if (markv_freq.count(seq))
        {
            markv_freq[seq][a]++;
        }
        else
        {
            markv_freq[seq][a] = 1;
        }

        // add symbol to memory
        if (symbols.length() > 0)
        {
            if (symbols.find(a) == string::npos) // symbol not found
            {
                symbols.push_back(a);
            }

        }
        else {
            symbols = a;
        }

        return 0;
    }

    /// @brief 
    /// @param mt model type, for file name  
    /// @return 
    int GenerateModel(string filename, string modelType, int k)
    {
        ofstream outputFile(filename);

        if (!outputFile.is_open()) {
            cout << "Error opening file for writing." << endl;
            return 1;
        }

        outputFile << modelType << endl;
        outputFile << to_string(k) << endl;

        outputFile << markv_freq.size() << std::endl;

        for (const auto& pair : markv_freq) {
            outputFile << pair.first << std::endl;

            outputFile << pair.second.size() << std::endl;

            for (const auto& innerPair : pair.second) {
                outputFile << innerPair.first << " ";
                outputFile << innerPair.second << std::endl;
            }
        }

        outputFile.close();

        return 0;
    }

    markovf()
    {
        symbols = "";
    }


};
#pragma endregion

#pragma region Declarations
// input parameters (defaults)
int k = 2;                  // Model order
string inputFilename = "none";   // File name
string modelType = "H";     // Model Type: (H) Human, (A) chatGPT/AI

// Markov model info
markovf markv_freq;
string w; // sliding window
unordered_map<string, string> inputflags;
#pragma endregion

string getFilename(const std::string& filePath) {
    int pos = filePath.find_last_of("\\/");
    if (pos != string::npos) {
        return filePath.substr(pos + 1);
    }
    else {
        return filePath;
    }
}

string getFilePath(const std::string& filePath) {
    int pos = filePath.find_last_of("\\/");
    if (pos != string::npos) {
        return filePath.substr(0,pos);
    }
    else {
        return filePath;
    }
}


#pragma region helper_functions
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
#pragma endregion

#pragma region MAIN
int main(int argc, char* argv[])
{

    // get input paramenters
    inputflags = getFlags(argc, argv);
    if (inputflags.count("f")) {
        inputFilename = inputflags.at("f");
    }
    else {
        cout << "FCM: No filename given\n";
        return 1;
    }

    if (inputflags.count("k")) {
        k = stof(inputflags.at("k"));
    }

    if (inputflags.count("t")) {
        modelType = inputflags.at("t");
    }

    cout << "FCM starting parameter set: " << endl;
    cout << "-> File: " << inputFilename << endl;
    cout << "-> k (window size): " << k << endl;
    cout << "-> t (modelType): " << modelType << endl;


    // read file to memory
    ifstream file(inputFilename);
    if (file.fail())
    {
        cout << "FCM: Error opening file: " << inputFilename;
        return 1;
    }

    string line;
    int length = 0;
    string window = "";
    char letter;

    while (file.get(letter)) {

        length = (int)window.length();
        if (length == k)
        {
            //cout << l << " " << k<<endl;
            markv_freq.Increment(window, letter);
        }

        // window management
        window += letter;
        //cout << "-- byte: " << b << "|window: " << w << endl;
        if (window.length() > k)
        {
            window.erase(0, 1);
        }
    }

    file.close();

    string filename = getFilename(inputFilename);
    string filepath = getFilePath(inputFilename);
    string outputFilename = "";

#ifdef _WIN32
    outputFilename = filepath + "\\";
#else
    outputFilename = filepath + "/";
#endif

    outputFilename = outputFilename + "ModelType_" + modelType + "_K_" + to_string(k) + "_" + filename;

    markv_freq.GenerateModel(outputFilename,modelType,k);

    return 0;
}
#pragma endregion
