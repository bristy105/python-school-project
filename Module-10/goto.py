
import rclpy
from math import atan2, pow, sqrt
from geometry_msgs.msg import Twist
from rclpy.node import Node
from turtlesim.msg import Pose


class TurtleBot(Node):

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
     	# Initialize the node
        super().__init__('turtlebot_controller')
        # node is created
        # rclpy.create_node('turtlebot_controller')
        self.publisher=self.create_publisher(Twist,'/turtle1/cmd_vel',10) 
        
        
        # # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        # self.velocity_publisher = self.Publisher(Twist,'/turtle1/cmd_vel')        #                                         )
        
        # # A subscriber to the topic '/turtSubscribere1/pose'. self.update_pose is called
        # # when a message of type Pose is received.
        self.pose_subscriber = self.create_subscription('/turtle1/pose', Pose, self.update_pose)
        
     


        self.pose = Pose()
        self.rate = rclpy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
    if __name__ == '__main__':

      try:      

            x = TurtleBot()
            x.move2goal()
      except:
        pass

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
       
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
       
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def move2goal(self):
        """Moves the turtle to the goal."""
        goal_pose = Pose()

        # Get the input from the user.
        goal_pose.x = float(input("Set your x goal: "))
        goal_pose.y = float(input("Set your y goal: "))
    
  
        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = input("Set your tolerance: ")

        vel_msg = Twist()#!/usr/bi


        
        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        


    if __name__ == '__main__':

      try:      

            x = TurtleBot()
            x.move2goal()
      except:
        pass