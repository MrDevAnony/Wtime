#include <chrono>
#include <cstdlib>
#include <iostream>
#include <string>
#include <format>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: wtime <command>\n";
        return EXIT_FAILURE;
    }
  
    std::string command;
    for (int i = 1; i < argc; ++i) {
        command += argv[i];
        if (i < argc - 1) command += ' ';
    }
  
    auto start = std::chrono::steady_clock::now();
    int result = std::system(command.c_str());
    auto end = std::chrono::steady_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
  
    std::cout << std::format("Elapsed time: {}.{:03} seconds\n",
                             duration.count() / 1000,
                             duration.count() % 1000);
    return result;
}
