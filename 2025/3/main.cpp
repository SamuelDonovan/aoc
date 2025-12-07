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

auto find_max(std::string& number, int start, int end) -> int 
{
    int maxIndex = start;
    for (int idx = start; idx < end; idx++) {
        if (number[idx] > number[maxIndex])
            maxIndex = idx;
    }
    return maxIndex;
}

auto find_max_in_line(std::string& number) -> int 
{
    auto firstIndex = find_max(number, 0, static_cast<int>(number.size()) - 1);
    auto secondIndex = find_max(number, firstIndex + 1, static_cast<int>(number.size()));
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
