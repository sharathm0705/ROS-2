#To send a message :
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class myNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello World !!!")



def main(args=None):
    rclpy.init(args=args)
    node=myNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__=="__main__":
    main()
    
