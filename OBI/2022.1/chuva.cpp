#include "bits/stdc++.h"

using namespace std;

#define fastio ios_base::sync_with_stdio(false), cin.tie(nullptr)

int main(){
    fastio;

    int n,s; cin >> n >> s;
    vector<int> arr;

    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        arr.push_back(x);
    }

    set<int> sum;
    map<int,int> mp;
    int aux = 0; mp[0]++; sum.insert(0);

    for(int i: arr){
        aux+=i;
        mp[aux]++;
        sum.insert(aux);
    }

    auto l = sum.begin(), r = sum.begin();
    int ans = 0;

    if(s == 0){
        for(int i: sum){
            int x = mp[i];
            ans += (x+1)*x/2;
            ans-=x;
        }
        cout << ans << '\n';
        return 0;
    }

    while(r != sum.end()){

        int k = (*r) - (*l);

        if(k == s){
            ans += (mp[*l] * mp[*r]);
        }

        if(k <= s) r++;
        else l++;
    }

    cout << ans << '\n';

    return 0;
}