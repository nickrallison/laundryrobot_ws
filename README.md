# laundryrobot_ws
## To initialize the driver 
1. Clone this repo to your home folder

2. Copy the contents of this folder to a sub directory called src

```
laundryrobot_ws
│
└───folder1
|   │   files...
│   
└───folder2
    │   files...
```

Change top to bottom

```
laundryrobot_ws
│
└───src
    │
    └───folder1
    |   │   files...
    | 
    └───folder2
        |   files...

```
 
3. In the laundryrobot_ws run catkin_make

4. Add ```source ~/laundryrobot_ws/devel/setup.bash``` to your bashrc

5. In two new windows, run ```roscore``` and ```roslaunch laundry_firmware rpmcontrol.launch```
