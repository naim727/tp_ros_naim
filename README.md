# tp_ros_naim

This package contains two nodes button_gui.py and talker.py

# To install this package

clone it into the src folder in your catkin workspace

`cd ~/catkin_ws/src`

`git clone https://github.com/naim727/tp_ros_naim.git`

`catkin build`

`source ~/catkin_ws/devel/setup.bash`

# To run the node and rviz

Once the setup file has been sourced.

`roscore` 

`roslaunch tp_ros_naim tp_ros_naim.launch`

# To run the nodes separately

talker.py node

`roscore` in one terminal

`rosrun tp_ros_naim talker.py`in another terminal

button_gui.py node

`roscore` in one terminal

`rosrun tp_ros_naim button_gui.py`in another terminal


