project(kdam-cpp)

add_custom_target(
    kdam_c_bindings
    COMMAND env CARGO_TARGET_DIR=${CMAKE_CURRENT_BINARY_DIR} cargo build --release
    WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}/kdam-c-bindings
    DEPENDS ${PROJECT_SOURCE_DIR}/kdam-c-bindings/src/lib.rs ${PROJECT_SOURCE_DIR}/kdam-c-bindings/Cargo.toml
    )
add_library(kdam kdam-cpp/kdam.cpp)
add_dependencies(kdam kdam_c_bindings)
target_link_libraries(kdam PRIVATE ${CMAKE_CURRENT_BINARY_DIR}/release/libkdam_c_bindings.a)

# TODO make it work
# add_executable(example kdam-cpp/example.cpp)
# target_link_libraries(example PRIVATE kdam)
