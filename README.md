# Stanford Robotics Suite

![gallery of_environments](resources/gallery.png)

Stanford Robotics Suite is a tookit and simulation benchmark powered by the [MuJoCo physics engine](http://mujoco.org/) for reproducible robotics research. The current release concentrates on reinforcement learning for robot manipulation.

Reinforcement learning has been a powerful and generic tool in robotics. Reinforcement learning combined with deep neural networks, i.e. *deep reinforcement learning* (DRL), has achieved some exciting successes in a variety of robot control problems. However, the challenges of reproducibility and replicability in DRL and robotics have impaired research progress. Our goal is to provide an accessible set of benchmarking tasks that facilitates a fair and rigorus evaluation and improves our understanding of new methods.

This framework was originally developed since late 2017 by researchers in [Stanford Vision and Learning Lab](http://svl.stanford.edu/) (SVL) as an internal tool for robot learning research. Today it is actively maintained and used for robotics research projects in SVL.

This release of Stanford Robotics Suite contains a set of benchmarking manipulation tasks and a modularized design of APIs for building new environments. We highlight these primary features below:

* [**standardized tasks**](RoboticsSuite/environments): a set of single-arm and bimanual manipulation tasks of large diversity and varying complexity.
* [**procedural generation**](RoboticsSuite/models): modularized APIs for programmatically creating new scenes and new tasks as a combinations of robot models, arenas, and parameterized 3D objects;
* [**controller modes**](RoboticsSuite/controllers): a selection of controller types to command the robots, such as joint velocity control, inverse kinematics control, and 3D motion devices for teleoperation;
* **multi-modal sensors**: heterogeneous types of sensory signals, including low-level physical states, RGB cameras, depth maps, and proprioception;
* **human demonstrations**: utilities for collecting human demonstrations, replaying demonstration datasets, and leveraging demonstration data for learning.

## Installation
TODO(Joan): Talk about system requirement, library dependencies, installation commands on Linux and Mac OS X.

## Quick Start
TODO(Anchit): A demo of how to import the framework and run the environment.

## Building Your Own Environments
TODO(Jiren): A short example of how to create a new environment.

## Human Demonstrations
#### Collecting human demonstrations

Demonstrations can be collected by either using a keyboard or using a [SpaceNavigator 3D Mouse](https://www.3dconnexion.com/spacemouse_compact/en/) with the [collect_human_demonstrations](RoboticsSuite/scripts/collect_human_demonstrations.py) script. It takes the following arguments.

- `directory:` path to a folder for where to store the pickle file of collected demonstrations
- `environment:` name of the environment you would like to collect the demonstrations for
- `device:` either "keyboard" or "spacemouse"
- `large:` if True, store both a demo.bkl file with the entire set of demonstrations and a demo.pkl file with indices into the demo.bkl file. This allows for on-demand loading of demonstrations, in case the set of demonstrations is too large to load into memory all at once.

**Keyboard controls**

Note that the rendering window must be active for these commands to work.

|   Keys   |              Command               |
| :------: | :--------------------------------: |
|    q     |          reset simulation          |
| spacebar |    toggle gripper (open/close)     |
| w-a-s-d  | move arm horizontally in x-y plane |
|   r-f    |        move arm vertically         |
|   z-x    |      rotate arm about x-axis       |
|   t-g    |      rotate arm about y-axis       |
|   c-v    |      rotate arm about z-axis       |
|   ESC    |                quit                |

**SpaceNavigator 3D Mouse controls**

|          Control          |                Command                |
| :-----------------------: | :-----------------------------------: |
|       Right button        |           reset simulation            |
|    Left button (hold)     |             close gripper             |
|   Move mouse laterally    |  move arm horizontally in x-y plane   |
|   Move mouse vertically   |          move arm vertically          |
| Twist mouse about an axis | rotate arm about a corresponding axis |
|      ESC (keyboard)       |                 quit                  |

 

#### Structure of collected demonstrations

Every set of demonstrations is collected as a `demo.pkl` file, and possibly with a corresponding`demo.bkl`. The reason for collecting both a `demo.pkl` and a `demo.bkl` file is that it allows us to avoid loading an entire set of demonstrations into memory all at once by storing a series of pickled demonstrations in the `demo.bkl` and their corresponding indices in the `demo.pkl`. This is useful if the set of demonstrations is large (for example, on the order of gigabytes) since we can operate on the indices in `demo.pkl` until we wish to load a demonstration, and then the demonstration can be loaded using the offset.



If no `demo.bkl` file is used, the `demo.pkl` file, once unpickled, will be a list of dictionaries. Each dictionary corresponds to a single demonstration. The contained keys are `model` and `states`. The `model` key stores the entire mujoco model as an xml string. This is useful for storing scene information necessary to reconstruct the demonstration state. The `states` key stores a list of mujoco states, ordered by time. 



If a `demo.bkl` file is used, the `demo.pkl` file, once unpickled, will be a list of indices. Each index corresponds to a single demonstration that is stored at that offset in the `demo.bkl` file. To read a demonstration, simply seek to its offset in the `demo.bkl` file and unpickle the file. As before, each demonstration is a dictionary with the keys `model` and `states`.



To see a simple example of how to read demonstrations, please see [demo_playback_demonstrations](RoboticsSuite/scripts/demo_playback_demonstrations.py).

#### Download CRIMSON dataset

We collected a large-scale dataset on the `SawyerPickPlace` and `SawyerNutAssembly` tasks using the [CRIMSON](https://crowdncloud.ai/) platform. Crowdsourced workers collected these task demonstrations remotely. It consists of **1070** successful `SawyerPickPlace` demonstrations and **1147** successful `SawyerNutAssembly` demonstrations.

We are providing the dataset in the hopes that it will be beneficial to researchers working on imitation learning. Large-scale imitation learning has not been explored much in the community; it will be exciting to see how this data is used.  

You can download the dataset [here](https://drive.google.com/open?id=1iZSXTQZfBVcIBC3dRF5xUqMmWCmW64PD).

Due to its large size, the dataset has `*.pkl` pickle files containing indices into the corresponding `*.bkl` pickle files, allowing for on-demand loading of demonstrations (instead of loading them all into memory at once). When running any code involving demonstrations, you should still use `*.pkl` file paths, and ensure that the corresponding `*.bkl` file is in the same directory. The dataset consists of the following pickle files:

- **pickplace-full.pkl, pickplace-full.bkl**
  - The set of complete demonstrations on the full `SawyerPickPlace` task. Every demonstration consists of the Sawyer arm placing one of each object into its corresponding bin.
- **pickplace-milk.pkl, pickplace-milk.bkl**
  - A postprocessed, segmented set of demonstrations that corresponds to the `SawyerPickPlaceMilk` task. Every demonstration consists of the Sawyer arm placing a can into its corresponding bin. 
- **pickplace-bread.pkl, pickplace-bread.bkl**
  - A postprocessed, segmented set of demonstrations that corresponds to the `SawyerPickPlaceBread` task. Every demonstration consists of the Sawyer arm placing a loaf of bread into its corresponding bin. 
- **pickplace-cereal.pkl, pickplace-cereal.bkl**
  - A postprocessed, segmented set of demonstrations that corresponds to the `SawyerPickPlaceCereal` task. Every demonstration consists of the Sawyer arm placing a cereal box into its corresponding bin. 
- **pickplace-can.pkl, pickplace-can.bkl**
  - A postprocessed, segmented set of demonstrations that corresponds to the `SawyerPickPlaceCan` task. Every demonstration consists of the Sawyer arm placing a can into its corresponding bin. 
- **nutassembly-full.pkl, nutassembly-full.bkl**
  - The set of complete demonstrations on the full `SawyerNutAssembly` task. Every demonstration consists of the Sawyer arm fitting a square nut and a round nut onto their corresponding pegs. 
- **nutassembly-square.pkl, nutassembly-square.bkl**
  - A postprocessed, segmented set of demonstrations that corresponds to the `SawyerNutAssemblySquare` task. Every demonstration consists of the Sawyer arm fitting a square nut onto its corresponding peg. 
- **nutassembly-round.pkl, nutassembly-round.bkl**
  - A postprocessed, segmented set of demonstrations that corresponds to the `SawyerNutAssemblyRound` task. Every demonstration consists of the Sawyer arm fitting a round nut onto its corresponding peg. 

#### Replay human demonstrations

We have included a generic utility script that shows how demonstrations can be played back. Our [demo_playback_demonstrations](RoboticsSuite/scripts/demo_playback_demonstrations.py) script selects demonstration episodes at random from a demonstration pickle file and replays them. We have included some sample demonstrations at `models/assets/demonstrations`.

#### Control start state distribution of environment with demonstration states

Several prior works have demonstrated the effectiveness of altering the start state distribution of training episodes for learning RL policies. We provide a generic utility for setting various types of learning curriculums which dictate how to sample from demonstration episodes when doing an environment reset. For more information see the `DemoSamplerWrapper` class. 

We have provided an example of how to use this wrapper along with a demonstration pickle file in the [demo_learning_curriculum](RoboticsSuite/scripts/demo_learning_curriculum.py) script.

## Citations
TODO(Yuke): Add bibtex for citing RoboticsSuite.
