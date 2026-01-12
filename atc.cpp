#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[]) {
    //Help
    if(argc == 1 || (string)argv[1] == "--help") {
        cout << "CPH — Competitive Programming CLI helper\n\n";
        cout << "Usage:\n";
        cout << "  atc <option> <problem_id>\n";
        cout << "Examples:\n";
        cout << "  atc abc213_a\n";
        return 0;
    }

    //Invalid number of arguments
    if(argc != 3) {
        cout<<"Usage Option:\n";
        cout<<"atc fetch <problem>\n";
        cout<<"atc test <problem>\n";
        cout<<"atc run <problem>\n";
        cout<<"Example: atc fetch abc202_b\n";
        return 0;
    }

    string cmd = argv[1];
    string prob = argv[2];
    if(prob.size() != 8) {
        cerr<<"⚠️  Invalid problem ID\n";
        return 1;
    }

    string contestid = prob.substr(0, 6);

    //fetch command
    if(cmd == "fetch") {
        string create_solcpp = "touch " + prob + ".cpp";
        string parsecmd = "python3 /opt/CPH/atc_parse.py " + prob;
        int parsecode = system(parsecmd.c_str());
        if(parsecode) {
            cerr<<"Fetch Failed\n";
            return 1;
        }
        int createcode = system(create_solcpp.c_str()); 
        if(createcode) {
            cerr<<"Unable to create .cpp Solution file\n";
            return 1;
        }
    }

    //run command
    else if(cmd == "run") {
        string compile = "g++ -std=c++23 -O2 " + prob + ".cpp" + " -o " + prob;
        string run = "./" + prob;
        int compilecode = system(compile.c_str());
        if(compilecode) {
            cerr<<"Compilation error\n";
            return 1;
        }
        int runcode = system(run.c_str());
        if(runcode) {
            cerr<<"Runtime error\n";
            return 1;
        }
    }

    //test command
    else if(cmd == "test") {
        int i = 1;
        int ac = 0;
        while(true) {
            string input = prob + to_string(i) + ".in";
            string output = prob + to_string(i) + ".ans";
            string checkcmd = "[ -f " + input + " ]";
            int checkcode = system(checkcmd.c_str());
            if(checkcode) {
                if(ac == i-1) cout<<"✅ ";
                else cout<<"❌ ";
                cout<<ac<<"/"<<i-1<<" Passed\n";
                return 0;
            }
            string testcmd = "/opt/CPH/run.sh " + prob + ".cpp " + input + " " + output;            
            int testcode = system(testcmd.c_str());
            if(testcode == 1) {
                cerr<<"Error while testing\n";
                return 0;
            }
            else if(!testcode) ac++;
            i++;
        }
    }

    //No commands matched
    else {
        cout<<"Commands available are fetch\nrun\ntest\n";
    }
    return 0;
}

