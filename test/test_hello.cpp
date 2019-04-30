#include <cstdlib>
#include "hello.hpp"

int main() {
    const std::string expected("Hello World");
    if (expected != say_hello()) {
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}