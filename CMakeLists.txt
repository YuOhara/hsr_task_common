cmake_minimum_required(VERSION 2.8.3)
project(hsr_task_common)
find_package(catkin REQUIRED COMPONENTS
  cmake_modules message_generation std_msgs std_srvs sensor_msgs
)


add_message_files(FILES
  UiOut.msg)
generate_messages(DEPENDENCIES sensor_msgs)
catkin_package(
)

install(DIRECTORY launch rvizconfig scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)

install(FILES Makefile
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
