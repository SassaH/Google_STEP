//
//  anagram.cpp
//
//
//  Created by 佐々日向子 on 2016/05/31.
//
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){
    string s, t, str, str2 = "_";
    ifstream reading_file;
    int x =0;
    
    cout << "16文字以下の文字列を入力してください：";
    cin >> s;
    
    t = s;
    sort(t.begin(),t.end());
    
    //cout << t << endl;

    reading_file.open("/usr/share/dict/words", ios::in); //open dictionary
    
    if (reading_file.fail())
    {
        cerr << "失敗" << endl;
        return -1;
    }
    while (getline(reading_file, str))
    {
        if(str.length() <= 16){ //cut words over 16.
            str2 = str;
            sort(str2.begin(),str2.end());
           /* if (str == "astronomer") {
                cout << "Found astronomer! str2 is " << str2 << " and t is " << t << " is eq? " << (str2 == t) << " s is " << s << endl;
            }*/
            if((str2 == t) && (str != s)){
                cout << str << endl;
                x++;
            }
        }
    }
    if(x==0){
        cout << "No words." << endl;
    }
    
    return 0;
}