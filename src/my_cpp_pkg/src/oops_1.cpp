//To print a message using OOPS :

#include "rclcpp/rclcpp.hpp"
class MyNode : public rclcpp::Node{
    public : 
    MyNode(): Node("oops_test")
    {
        RCLCPP_INFO(this->get_logger(),"Hello World !!!");
    }
    private:
};

int main(int argc,char** argv){
    rclcpp::init(argc,argv);
    auto node = std::make_shared<MyNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}