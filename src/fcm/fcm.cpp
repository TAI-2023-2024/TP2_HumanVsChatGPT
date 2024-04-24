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
        unordered_map<string,unordered_map<char, uint64_t>> markv_freq;

    public:
        int Increment(string seq, char a)
        {
            if(markv_freq.count(seq))
            {
                markv_freq[seq][a] ++;
            }
            else
            {
                markv_freq[seq][a] = 1;
            }

            // add symbol to memory
            if (symbols.length()>0)
            {
                if(symbols.find(a) == string::npos) // symbol not found
                {
                    symbols.push_back(a);
                }

            }else{
                symbols = a;
            }

            return 0; 
        }

        /// @brief 
        /// @param mt model type, for file name  
        /// @return 
        int GenerateModel(string mt = "")
        {
            ofstream f ("fcm.txt");
            
            if(f.fail())
            {
                cout << "FCM\\markovf: file open failed";
                return 1;
            }
            // set header
            string fileHeader = "Seq";
            for (int i = 0 ;i<symbols.length();i++)
            {
                fileHeader = fileHeader + separator + symbols[i];
            }
            // generate a txt file with the model data
            string line = "";
            ostringstream oss;
            for (auto s = markv_freq.begin(); s != markv_freq.end(); s++)
            {                
                // sequence
                line= line + s->first;
                // values for each symbol
                for (int i = 0 ;i<symbols.length();i++)
                {
                    oss << s->second[symbols[i]];
                    line = line + separator + oss.str();
                    oss.flush();
                }
                line = line + '\r' + '\n';
                
                //append to file
                f<< line;
            }
            
            f.close();

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
float alpha = 0.5;          //smoothing factor
int k = 2;                  // Model order
string filename = "none";   // File name
string modelType = "H";     // Model Type: (H) Human, (A) chatGPT/AI

// Markov model info
markovf markv_freq;
string w; // sliding window
unordered_map<string, string> inputflags;
#pragma endregion



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
    inputflags = getFlags(argc,argv);
    if (inputflags.count("f") ) {
        filename = inputflags.at("f");
    }
    else {
        cout << "FCM: No filename given\n";
        return 1;
    }

    if (inputflags.count("a")) {
        alpha = stof(inputflags.at("a"));
    }
    
    if (inputflags.count("k")) {
        k = stof(inputflags.at("k"));
    }

    cout<< "FCM starting parameter set: " << endl;
    cout<< "-> File: "<< filename << endl;
    cout<< "-> k (window size): "<< k << endl;
    cout<< "-> a (smoothing factor): "<< alpha << endl;

    // read file to memory
    ifstream file(filename);    
    if ( file.fail() )
    {
        cout << "FCM: Error opening file: "<< filename;
        return 1;
    }

    // get file size
    filebuf* file_buf = file.rdbuf();
    uint64_t file_size = file_buf->pubseekoff(0,file.end);
    // reset buffer position
    file_buf->pubseekpos(0);

    // auxiliar byte reader
    char b;

    // auxiliar counter to end process in case of file buffer change
    uint64_t auxc = 0;
    int l = 0;
    w = "";
    do{
        // check file 
        if(auxc >= file_size)
        {
            cout<<"FCM: Buffer was corrupted. Process terminated.";
            file.close();
            //break;
            return 1;            
        }

        b = file_buf->sgetc();        

        // markov model update        
        l = (int)w.length();
        if (l == k) 
        {
            cout << l << " " << k<<endl;
            markv_freq.Increment(w,b);
        }

        // window management
        w.push_back(b);
        cout << "-- byte: " << b << "|window: " << w << endl;
        if (w.length() > k) 
        {
            w.erase(0, 1);
        }

        cout << "-- byte: " << b << "|window: " << w << endl;

    }while(file_buf->snextc() != EOF);
    
    file.close();

    markv_freq.GenerateModel("Test_");

    return 0;
}
#pragma endregion