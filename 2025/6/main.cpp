#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <print>
#include <stdexcept>
#include <numeric>

    std::vector<std::vector<std::string>>
read_rows(const std::string& filename)
{
    std::ifstream in(filename);
    if (!in) {
        throw std::runtime_error("Could not open file");
    }

    std::vector<std::vector<std::string>> rows;
    std::string line;

    while (std::getline(in, line)) {
        std::istringstream iss(line);
        std::vector<std::string> row;
        std::string token;

        while (iss >> token)
            row.push_back(token);

        rows.push_back(std::move(row));
    }

    return rows;
}

    std::vector<std::vector<std::string>>
transpose(const std::vector<std::vector<std::string>>& rows)
{
    if (rows.empty())
        return {};

    size_t cols = rows[0].size();
    std::vector<std::vector<std::string>> columns(cols);

    for (const auto& row : rows) {
        for (size_t c = 0; c < cols; ++c)
            columns[c].push_back(row[c]);
    }

    return columns;
}

std::vector<std::string> concat_column_numbers(const std::vector<std::string>& col)
{
    if (col.empty()) return {};
    std::string concatenated;

    // All except last element
    for (size_t i = 0; i < col.size() - 1; ++i)
        concatenated += col[i];

    // Add operator as a separate element
    return { concatenated, col.back() };
}

std::vector<std::vector<std::string>> parse_file_concat(const std::string& filename)
{
    auto rows = read_rows(filename);
    auto cols = transpose(rows);

    std::vector<std::vector<std::string>> result;

    for (auto& col : cols) {
        result.push_back(concat_column_numbers(col));
    }

    return result;
}

auto part1() -> uint64_t
{
    auto rows = read_rows("input.txt");
    auto cols = transpose(rows);
    std::vector<uint64_t> results;
    for (auto& col : cols)
    {
        std::reverse(col.begin(), col.end());
        auto operand = col[0];
        col.erase(col.begin());
        uint64_t result;
        if ("+" == operand)
        {
            result = std::accumulate(col.begin(), col.end(), uint64_t{0},
                    [](uint64_t acc, const std::string& s) {
                    return acc + std::stoull(s);
                    });
        } else {
            result = std::accumulate(col.begin(), col.end(), uint64_t{1},
                    [](uint64_t acc, const std::string& s) {
                    return acc * std::stoull(s);
                    });

        };
        results.push_back(result);
    }
    return std::accumulate(results.begin(), results.end(), uint64_t{0});
}

int main()
{
    std::println("Part 1 is {}", part1());
    return 0;
}
