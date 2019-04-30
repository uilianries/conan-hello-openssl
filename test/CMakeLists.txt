cmake_minimum_required(VERSION 2.8)
project(test_hello CXX)

add_executable(${PROJECT_NAME} test_hello.cpp)
target_link_libraries(${PROJECT_NAME} hello)

add_test(NAME test_all
        COMMAND ./test_hello)