cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)
add_executable(oops_1 src/oops_1.cpp)
ament_target_dependencies(oops_1 rclcpp)
add_executable(oops_2 src/oops_2.cpp)
ament_target_dependencies(oops_2 rclcpp)


install(TARGETS 
    cpp_node
    oops_1
    oops_2
    DESTINATION lib/${PROJECT_NAME}
)

ament_package()
