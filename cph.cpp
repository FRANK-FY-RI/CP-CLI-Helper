#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char* argv[]) {

    if (argc < 2) {
        cout << "Use --help for usage\n";
        return 0;
    }

    if(string(argv[1]) == "--help") {
        cout<<"CPH - Competitive Programming CLI helper\n\n";
        cout<<"Features:";
        cout<<"fetch\nrun\ntest\n";
        cout<<"Platforms Supported:\n";
        cout<<"Codeforces: cf\n";
        cout<<"Atcoder: atc\n";
        return 0;
    }

    if(argc !=4) {
        cout<<"Usage:\n";
        cout<<"cph <platform> <option> <problem_id>\n";
        cout<<"Example:\n";
        cout<<"cph cf fetch 4A\n";
        cout<<"cph atc fetch abc200_a\n";
        return 0;
    }

    if(string(argv[1])!="cf" && string(argv[1])!="atc") {  
        cout<<"Platforms Supported:\n";
        cout<<"Codeforces: cf\n";
        cout<<"Atcoder: atc\n";
        return 0;
    }
    string platform = argv[1];
    string checkcmd = "test -f /opt/CPH/" + platform;
    int checkcode = system(checkcmd.c_str());
    if(checkcode) {
        string compilecmd = "sudo g++ -std=c++23 -O3 /opt/CPH/" + platform + ".cpp -o /opt/CPH/" + platform;
        int compilecode = system(compilecmd.c_str());
        if(compilecode) {
            cerr<<"Binary file " <<platform<<" not found and unable to compile "<<platform<<".cpp\n";
            return 1;
        }
    }
    string cmd = argv[2];
    string problem = argv[3];
    string runcmd = "/opt/CPH/" + platform + " " + cmd + " " + problem;
    int runcode = system(runcmd.c_str());
    return 0;
}
