## Research Track-1/Fall'22/First Assignment ##

# Description #

The purpose of that project is to build a program, that grabs the silver tokens and release them to the nearest golden token with respectively. When the all silver tokens will be released near to the golden tokens the process will stops.

# Installing #

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

# Running #

To run one or more scripts in the simulator, use `run.py`, passing it the file names.

You can run the program with:
```bash
$ python2 run.py firstassignment.py
```

# How it's works #

At the beginning of the code there is three trasholds, and two arrays of offsets has been defined to use them later. The aim of that trasholds and arrays can be seen with the commands which are in the code. After that for robot's linear and angular velocity has been defined by creating two different funcions. Before the main part of the code, there is two more functions for robots seeing the silver and the golden tokens. In these functions there is a condition to understand which token is the robot looking for and token.info.marker type has been used exatly for that purpose. By adding the offset line to these functions, the robot become able to select each token just for one time. This logic is working for silver and the golden token both. 

The main part of the code is starting by the while loop, in the while loop there is possible three situation, to find silver token, to find golden token or to ending the program. 

The code is starting the state which is 'silver is true' means that the robot starts to look for silver token.  If the distance between the robot and the silver token is less than trashold then robots grabs the silver token and adds it's offset to the offset_S array. 

In the second situation the robot is looking for the golden token, if the distance between the robot and the golden token is less than the golden_trashhold then the robot will release the grabbed silver token near to the golden token. This golden token's offset is adding to the offset_G array. 

In the third situation if the array lengt of the silver and the golden offset equal to six it means that all the 6 silver boxes and all the 6 golden boxes had been processed and mission is completed. 

# Flow Chart #
The flow chart of the code can be reachable by using the link below.   
![alt text](https://github.com/barisakerr/research_track_assignment1/blob/main/flowchart.png)
