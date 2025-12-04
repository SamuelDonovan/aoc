#include <string>
#include <print>
#include <vector>
#include <iostream>
#include <fstream>
#include <stdexcept>

auto read_file_lines(const std::string& filename) -> std::vector<std::string>
{
    std::ifstream file(filename);
    if (!file.is_open()) {
        throw std::runtime_error("Failed to open file: " + filename);
    }

    std::vector<std::string> lines;
    std::string line;

    while (std::getline(file, line)) {
        lines.push_back(line);
    }

    return lines;
}

auto find_max(std::string& number, bool first, int skip = -1) -> int 
{
    int maxIndex = skip + 1;
    size_t reserve = 1 ? first : 0;
    for (int idx = skip + 1; static_cast<size_t>(idx) < number.size() - reserve; idx++) {
        if (number[idx] > number[maxIndex])
            maxIndex = idx;
    }
    return maxIndex;
}

auto find_max_in_line(std::string& number) -> int 
{
    auto firstIndex = find_max(number, true);
    auto secondIndex = find_max(number, false, firstIndex);
    return ((number[firstIndex] - '0') * 10) + (number[secondIndex] - '0');
}


auto part1() -> int
{
    auto file = read_file_lines("input.txt");
    int total = 0;
    for (auto number: file)
    {
        total += find_max_in_line(number);
    }
    return total;
}

int main()
{
    std::println("Part 1 is {}", part1());
    return 0;
}
