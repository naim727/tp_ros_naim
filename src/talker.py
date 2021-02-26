#!/usr/bin/env python
  
   import math
   import rospy
   from std_msgs.msg import String
   from geometry_msgs.msg import PoseStamped
    
    def talker():
        pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
        rospy.init_node('talker', anonymous=True)
        rate = rospy.Rate(15) # 15hz
        sub = rospy.Subscriber("button_gui", Bool,queue_size=1)
	msg = PoseStamped()
	l = 5
	msg.pose.position.x = 0
	msg.pose.position.y = 0
	
       while not rospy.is_shutdown():
		while sub == False:
			rate.sleep() 
	  
	        while sub == True
			if(point.pose.position.x == 0 & point.pose.position.y == 0):
				if(point.pose.position.y != l):
					point.pose.position.y = p1
					p1 = p1 + 1
					pub.publish(point)
					rate.sleep()
			
				elif(point.pose.position.x != l):
					point.pose.position.x = p2
					p2 = p2 + 1
					pub.publish(point)
					rate.sleep()
		
          		elif(point.pose.position.x == l & point.pose.position.y == l):
				if(point.pose.position.y != 0):
					p1 = p1 - 1
					point.pose.position.y = p1
					pub.publish(point)
					rate.sleep()
				elif(point.pose.position.x != l):
					p2 = p2 - 1
					point.pose.position.x = p2
					pub.publish(point)
					rate.sleep()
           
   if __name__ == '__main__':
       try:
           talker()
       except rospy.ROSInterruptException:
           pass

