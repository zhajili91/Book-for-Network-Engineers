"""
Task 17.3a
Create a generate_topology_from_cdp function that processes the
show cdp neighbor command output from multiple files and writes
the resulting topology to a single dictionary.
The generate_topology_from_cdp function must be created with parameters:
* list_of_files - list of files from which to read the output of the sh cdp neighbor command
* yaml_file is the name of the YAML file where the topology will be saved.
  * default is None. By default, the topology is not saved to a file.
  * topology is saved only if save_to_filename is file name as argument
The function should return a dictionary that describes the connections between
devices, regardless of whether the topology is saved to a file.
Dictionary example:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}
Interfaces must be written with a space. That is, so Fa 0/0, and not so Fa0/0.
Check the work of the generate_topology_from_cdp function on the list of files:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt
Check the operation of the save_to_filename parameter and write the resulting
dictionary to the topology.yaml file. You will need it in the next task.
"""
from pprint import pprint
from task17_3 import parse_sh_cdp_neighbors
import yaml
import glob

"""
First program with single txt file
"""


def generate_topology_from_cdp(cdp_output, save_to_filename):
    with open(save_to_filename,"w") as f:
        yaml.dump(parse_sh_cdp_neighbors(cdp_output), f, default_flow_style=False)
    with open('dictionary_to_yaml.yaml') as k:
        return k.read()


if __name__ == "__main__":
    sh_cdp_files = glob.glob("sh_cdp*")
    print(generate_topology_from_cdp("sh_cdp_sw1.txt", "dictionary_to_yaml.yaml"))
