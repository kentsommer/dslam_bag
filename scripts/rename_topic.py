#!/usr/bin/env python

from rosbag import Bag

with Bag('correctodom_wide_flat.bag', 'w') as bag:
    for topic, msg, t in Bag('original.bag'):
        if topic == '/image_left4':
            bag.write('image_left', msg, t)
        elif topic == '/image_right4':
            bag.write('image_right', msg, t)
        else:
            bag.write(topic, msg, t)
