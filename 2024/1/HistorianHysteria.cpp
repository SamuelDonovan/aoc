//--- Day 1: Historian Hysteria ---
#include <algorithm>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <numeric>

int main() {
    std::vector<int> left, right, diff;
    std::ifstream file("input.txt");
    std::string line, word;

    while (std::getline(file, line)) {
        std::istringstream iss(line);
        iss >> word;
        left.push_back(stoi(word));
        iss >> word;
        right.push_back(stoi(word));
    }

    file.close();
    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());
    
    for (int idx = 0; idx < left.size(); idx++) {
        diff.push_back(abs(left[idx] - right[idx]));
    }
    int sum = std::accumulate(diff.begin(), diff.end(), 0);
    printf("%d\n", sum);

// --- Part Two --- 
    int sim = 0;
    for (int idx = 0; idx < left.size(); idx++) {
        auto it = std::find(right.begin(), right.end(), left[idx]);
        sim += *it * std::count(right.begin(), right.end(), *it);
    }
    printf("%d\n", sim);
   

    return 0;
}

