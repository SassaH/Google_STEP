//
//  anagram.cpp
//
//
//  Created by 佐々日向子 on 2016/05/31.
//
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*引数string 返り値string
    渡されたstring型をabc順にソートしてstring型に戻して返す関数*/
string sort(string str){
    string str2;
    vector<string> v;
    
    for(int i=0;i<16;i++){
        v.push_back(str.substr(i,1));
    }
    sort(v.begin(),v.end());
    
    str2 = v[0];
    for(int j=1;j<16;j++){
        str2 = str2 + v[j];
    }
    return str2;
}

int main(){
    string s, t, str, str2;
    //ifstream reading_file; //?
    
    cout << "16文字以下の文字列を入力してください：";
    cin >> s;
    
    t = sort(s);
    
    cout << t << endl;
    
    
    //reading_file.open("/usr/share/dict/words", ios::in); //辞書を開く
    
  /*  if (ifs.fail())
    {
        cerr << "失敗" << endl;
        return -1;
    }
    while (getline(ifs, str))
    {
        str2 = sort(str);
        if(str2 == t) && (str != s){
            cout << str << endl;
        }
    }*/
    
    return 0;
}