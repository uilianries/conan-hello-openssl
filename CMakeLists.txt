cmake_minimum_required(VERSION 2.8)
project(hello CXX)

add_library(${PROJECT_NAME} hello.cpp hello.hpp)
target_include_directories(${PROJECT_NAME} PUBLIC ${CMAKE_SOURCE_DIR})

enable_testing()
add_subdirectory(test)