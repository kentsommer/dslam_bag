cmake_minimum_required(VERSION 2.8.3)
project(dslam_bag)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  dslam_ecto_vision
  dslam_ecto_bridge
  ecto
  ecto_opencv
  ecto_ros
  rostime
  sensor_msgs
)


catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES dslam_bag
#  CATKIN_DEPENDS dslam_ecto_vision/ ecto ecto_opencv/ ecto_ros/
#  DEPENDS system_lib
)
include_directories(${catkin_INCLUDE_DIRS})
catkin_python_setup()

##############################################################################
# Sources
##############################################################################

add_subdirectory(src)

##############################################################################
# Installs
##############################################################################

install(PROGRAMS
            scripts/dslam_bag
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
       )

install(DIRECTORY launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY bags
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
        PATTERN *.bag EXCLUDE
        PATTERN *.yaml EXCLUDE
)

install(DIRECTORY rviz
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
