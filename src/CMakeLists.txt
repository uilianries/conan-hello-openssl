cmake_minimum_required(VERSION 2.8)
project(MyHello CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(hello hello.cpp)
target_link_libraries(hello PUBLIC ${CONAN_LIBS})

install(FILES hello.h DESTINATION include/hello)

install(TARGETS hello
        RUNTIME DESTINATION bin
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib)