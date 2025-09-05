#To send message continuously :
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("Py_test")
        self.counter_=0
        self.get_logger().info("Hello World ")
        self.create_timer(1.0,self.callback_timer)

    def callback_timer(self):
        self.get_logger().info("Hello World "+str(self.counter_))
        self.counter_+=1



def main(args=None):
    rclpy.init(args=args)
    node=MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

