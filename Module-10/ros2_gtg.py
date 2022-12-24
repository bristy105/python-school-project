# Import libraries 
import rclpy                                # ROS2-Python interface
import math                                 # Python math library
import sys                                  # Python system library
from rclpy.node import Node                 # ROS2-Python interface node
from geometry_msgs.msg import Pose          # Geometry msg library
from geometry_msgs.msg import Twist         # - || - 
from nav_msgs.msg import Odometry           # Navigation odometry library
import numpy as np                          # Numpy (math library)
import matplotlib.pyplot as plt             # Plotting library

# Class which is used to represent goal point
class GoalPoint:
  def __init__(self, x, y, th):
    self.x = x
    self.y = y
    self.th = th

# "GoForward" class inherits from the base class "Node"
# This class is used to subscribe and publish control values for turtlebot
class GoToGoal(Node):

    # Constructor, when object is created
    def __init__(self):
    	# Initialize the node
        super().__init__('GTG_Publisher')

        # Initialize the publisher and subscriber
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(Odometry, '/odom', self.subPositionListener, 10)

        # Initialize a timer that excutes callback function every 500 milliseconds
        self.timer = self.create_timer(0.5, self.goToGoal)

        # Variable for robot position and orientation odometry 
        self.pose = Pose()                      # Robot position             
        self.theta = 0.0                        # Robot theta position
        self.state = 0                          # State of predefined 
        
        # Create arrays for plotting data
        self.error = []                         # List of euclidian distance values
        self.vel_lin = []                       # List of linear velocities
        self.vel_ang = []                       # List of angula velociites 
        self.x = []                             # List of robot x position 
        self.y = []                             # List of robot y position
        self.th = []                            # List of robot theta orientation

    # Callback function, which is triggered when a new position is published
    def subPositionListener(self, msg):
        # Position
        self.pose.position.x = msg.pose.pose.position.x
        self.pose.position.y = msg.pose.pose.position.y
        self.pose.position.z = msg.pose.pose.position.z

        # Orientation
        self.pose.orientation.w = msg.pose.pose.orientation.w
        self.pose.orientation.x = msg.pose.pose.orientation.x
        self.pose.orientation.y = msg.pose.pose.orientation.y
        self.pose.orientation.z = msg.pose.pose.orientation.z

        # Quaternion -> Euler angle
        t1 = +2.0 * (self.pose.orientation.w * self.pose.orientation.z + self.pose.orientation.x * self.pose.orientation.y)
        t2 = +1.0 - 2.0 * (self.pose.orientation.y * self.pose.orientation.y + self.pose.orientation.z * self.pose.orientation.z)
        self.theta = math.atan2(t1, t2)   # rad

        #self.get_logger().info("X:{0}\tY:{1}\tTH:{2}".format(round(self.pose.position.x,2),round(self.pose.position.y,2),round(self.theta,2)))
    
    # This function calculates the distance between robot position and goal position
    def euclidean_distance(self, goal_pose):
        return math.sqrt(pow((goal_pose.x - self.pose.position.x), 2) + pow((goal_pose.y - self.pose.position.y), 2))
    
    # Calculate the linear velocity of robot (const is the velocity amplifier)
    def linear_vel(self, goal_pose, constant):
        return constant * self.euclidean_distance(goal_pose)

    # Calculat steering angle, by atan() goal's and robot's positions
    # Notice that atan2 has first y and then x pos!!!
    def steering_angle(self, goal_pose):
        return math.atan2(goal_pose.y - self.pose.position.y, goal_pose.x - self.pose.position.x)

    # Calculate the angular velocity 
    def angular_vel(self, goal_pose):
        angleDiff = (self.steering_angle(goal_pose) - self.theta)
        return angleDiff 



    # Main go-to-goal function
    def goToGoal(self):

        # Initialization of goal point args(float x, float y, float th). NOTICE! th is in radians!!!
        if len(sys.argv) > 1:
            goal_pose = GoalPoint(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]))
        else:
            # Way points of square in the world
            # Start point   -2.0    -0.5    0
            #               -1.6    1.6     0
            #               1.6     1.6     -1.57
            #               1.6     -1.6    -3.142
            #               -1.6    -1.6    1.57
            if(self.state == 0):
                goal_pose = GoalPoint(-1.6,1.6,0)
            elif(self.state == 1):
                goal_pose = GoalPoint(1.6,1.6,-1.57)
            elif(self.state == 2):
                goal_pose = GoalPoint(1.6,-1.6,-math.pi)
            elif(self.state == 3):
                goal_pose = GoalPoint(-1.6,-1.6,1.57)
                

        # Tolerance parameter
        distance_tolerance = 0.08
        angular_tolerance = 0.01

        # K coefficient (magnitude of control)
        K_vel_coef = 0.25
        K_ang_coef = 1.5

        vel_msg = Twist()

       # Send info to logger, what are the euclidean distance and tolerance values
        self.get_logger().info("Euclidean distance: " + str(round(self.euclidean_distance(goal_pose),2)) + " Tolerance: " + str(distance_tolerance))
        
        # If robot is not at the goal, control kicks in
        if(self.euclidean_distance(goal_pose) > distance_tolerance):

            # Velocity control
            vel_msg.linear.x = self.linear_vel(goal_pose,K_vel_coef)
           
            # Angle control    
            # Normalize the angle difrence value
            angle = self.angular_vel(goal_pose)
            if(angle > math.pi):
                angle -= 2*math.pi
            elif(angle < -math.pi):
                angle += 2*math.pi

            vel_msg.angular.z = K_ang_coef*(angle)

            # Prompting the robot goal positions.
            self.get_logger().info("Controlling to... X:{0} - Y:{1} - TH:{2}".format(round(goal_pose.x,2),round(goal_pose.y,2),round(goal_pose.th,2)))
        
        elif(abs(goal_pose.th-self.theta) > angular_tolerance):
            # Robot is in correct xy position, but theta angle is wrong:
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = goal_pose.th-self.theta

            # Prompt the thate values of the robot and goal theta
            self.get_logger().info("Turning to TH:{0}".format(round(goal_pose.th,2)))
        else: 
            # robot at goal and has correct orientation
            self.get_logger().info("Goal reached! - Stopping/Switching...")
            vel_msg.linear.x = 0.0
            vel_msg.angular.z = 0.0

            if(self.state == 0):
                self.get_logger().warn("Switching state...")
                self.state = 1
            elif(self.state == 1):
                self.get_logger().warn("Switching state...")
                self.state = 2
            elif(self.state == 2):
                self.get_logger().warn("Switching state...")
                self.state = 3
            elif(self.state == 3):
                self.get_logger().warn("Switching state...")
                self.state = 0

            # self.timer.cancel()
            # quit()
        # Set the control values to list (for plotting at the end)
        self.error.append(self.euclidean_distance(goal_pose))
        self.vel_lin.append(vel_msg.linear.x)
        self.vel_ang.append(vel_msg.angular.z)
        self.x.append(self.pose.position.x)
        self.y.append(self.pose.position.y)
        self.th.append(self.theta)

        # Publish the controls to /cmd_vel topic 
        self.publisher.publish(vel_msg)

        
    def stop_turtlebot(self):
    	# define what happens when program is interrupted
    	# log that turtlebot is being stopped
        self.get_logger().info('stopping turtlebot')
    	# publishing an empty Twist() command sets all velocity components to zero
    	# Otherwise turtlebot keeps moving even if command is stopped
        self.publisher.publish(Twist())
    	
    
def main(args=None):
    rclpy.init(args=args)
    
    # we are using try-except tools to  catch keyboard interrupt
    try:
    	# create an object for GoForward class
        node_gtg = GoToGoal()
    	# continue untill interrupted
        rclpy.spin(node_gtg)
    	
    except KeyboardInterrupt:
    	# execute shutdown function
        node_gtg.stop_turtlebot()
    	# clear the node
        node_gtg.destroy_node()
        rclpy.shutdown()

    # Transfer python list into numpy array
    error = np.array(node_gtg.error)
    vel_lin = np.array(node_gtg.vel_lin)
    vel_ang = np.array(node_gtg.vel_ang)
    x = np.array(node_gtg.x)
    y = np.array(node_gtg.y)
    th = np.array(node_gtg.th)

    # Calculating the x-axel linespace with numpy arange
    t = np.arange(0, (error.size)/2, 0.5)

    # Plotting firts figure, which shows the eucledian distance (error between robot position and the goal)
    fig = plt.figure(1)
    ax = plt.gca()
    ax.axhline(y=0.08, color='r', linestyle='--')
    ax.plot(t, error, label='Error distance')
    plt.legend()

    # Figure two, shows the linear and angular velocities
    fig2 = plt.figure(2)
    ax = plt.gca()
    ax.plot(t, vel_lin, label='Linear velocity')
    ax.plot(t, vel_ang, label='Angular velocity')
    plt.legend()

    # Figure three, shows the robots position during the simulation
    fig3 = plt.figure(3)
    ax = plt.gca()
    ax.plot(t, x, label="Robot's position x")
    ax.plot(t, y, label="Robot's position y")
    ax.plot(t, th, label="Robot's orientation theta")
    plt.legend()

    # Show the plots
    plt.show()

# Main Function
if __name__ == '__main__':
    main()
