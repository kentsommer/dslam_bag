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
