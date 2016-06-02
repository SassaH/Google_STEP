#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){
    string s, t, str, str2, ans, ans2;
    ifstream reading_file;
    
    cout << "16文字以下の文字列を入力してください：";
    cin >> s;
    
    t = s;
    sort(t.begin(),t.end());
    
    ans2 = t.substr(1,1);

    reading_file.open("/usr/share/dict/words", ios::in); //open dictionary
    
    if (reading_file.fail())
    {
        cerr << "失敗" << endl;
        return -1;
    }
    while (getline(reading_file, str)){
        if(str.length() <= s.length()){
            str2 = str;
            sort(str2.begin(),str2.end());
            
            if((str2 == t) && (str != s)){
                ans=str;
                ans2=str2;
                cout << ans << endl;
            }else if(t.find_first_not_of(str2)>t.find_first_not_of(ans2)){
                ans = str;
                ans2 = str2;
            }
        
        }
    }
    
    cout << ans << endl;
    
    return 0;
}