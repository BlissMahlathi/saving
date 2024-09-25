#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
using namespace std;

// Define the audit criteria
map<string,vector<string>> audit_criteria ={
    {"Financial Statement",{"Accurate", "Complete", "Timely"}},
    {"Internal Control",{"Effective", "Efficient", "Compliant"}},
    {"Compliance",{"Regulatory","Legal","Ethical"}}
     };
map<string,vector<string>> audit_questions = {
    {"Financial Statement",{"Are financial statement acuurate? ", 
                           "Are financial statement complete? ", 
                            "Are financial statement timely? "}},
    {"Internal Control",{"Are internal control effective?",
                         "Are internal control efficient? ",
                          "Are internal control compliant? "}},
    {"Compliance",{"Is the organization compliant with regulations? ",
                    "Is the organization compliant with the laws? ",
                    "Is the organization compliant with the ethical standards? "}}
                  };
// Define the audit ratings
map<string,int>audit_ratings = {
    {"Yes",1},
    {"No",0},
    {"N/A",-1}
};
// conduct the audit
map<string, vector<int>> conduct_audit(){
    map<string,vector<int>> audit_results;
    for (auto& category : audit_questions) {
        vector<int> results;
        for (auto& question : category.second){
            string answer;
            cout << question << "(Yes/No/N/A): ";
            cin >> answer; 
            results.push_back(audit_ratings[answer]);
        }
    audit_results[category.first] = results;  
    }
    return audit_results;
}
// generate the audit report
void generate_report( const map<string, vector<int>>& audit_results){
    ofstream file("audit_report.csv");
    file << "Category","Criteria","Result"; 
    for (auto& category : audit_results){
        for (int i = 0; i < category.second.size(); ++i){
            file << category.first << "," << audit_criteria[category.first][i] << "," << category.second[i] << "\n";
        }
    }
    file.close();
    cout << "Audit report generated successfully!" << endl;
}

int main() {
    map<string,vector<int>> audit_results = conduct_audit();
    generate_report(audit_results);
    return 0;
}