from conans import ConanFile, CMake, tools


class FooConan(ConanFile):
    name = "foo"
    version = "0.1.0"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"
    requires = "OpenSSL/1.0.2q@conan/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
