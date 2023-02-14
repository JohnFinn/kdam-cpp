from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout


class KdamCppConan(ConanFile):
    name = "kdam-cpp"
    version = "0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of KdamCpp here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "kdam-cpp/*", "kdam-c-bindings/*"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("kdam.hpp", src="kdam-cpp", dst="include")
        self.copy("libkdam.a", src="", dst="lib")
        self.copy("libkdam_c_bindings.a", src="release", dst="lib")

    # TODO get rid of kdam_c_bindings
    def package_info(self):
        self.cpp_info.libs = ["kdam", "kdam_c_bindings"]
