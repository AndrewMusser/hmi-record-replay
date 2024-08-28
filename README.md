# Overview
You can use the scripts in this repo to record and replay user interactions with a machine HMI that is served over VNC. This can be useful for automated testing. 

# Usage
The `src/plc` folder contains a simple B&R Automation Studio project that can be run in simulation. Once built and running, this simulator serves a one-page HMI to VNC clients on port 5900. 

The `src/automation` folder contains the Python scripts required to record interactions with the HMI, and replay them later. 