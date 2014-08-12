## D(damn)SLAM with ROSBag support

Quickly and easily ROSBAG incoming DSLAM image and /odom feeds. 

## Usage

* Optional arguments:
    * -h : show help message
    * -b : bag incoming images and /odom
    * -front : use the front camera pair (left, right). Can be used with or without -back
    * -back : use the back camera pair (left, right). Can be used with or without -front

* To run:
    * ./dslam_image_capture_bag.py
    

## Tips

* Do not bag full point clouds, hard drives can't write (~120MB/s) at the same rate as the data (~290MB/s).

## FAQ

*Loopback Jumps*

If dslam works well on a bag that returns the robot to its initial position, then because of drift, it might have odom value of (0.0, 0.25).
When the odom is reset, then dslam will have thought the robot has gone from 0.25->0.0, i.e. 'jumped' by -0.25 and so will teleoport the
robot appropriately.