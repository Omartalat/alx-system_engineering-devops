# 0x00. Shell, Basics

This project is part of the curriculum of Holberton School. The goal is to learn the basics of the shell including navigation, file handling, and simple scripting.

## Description

This repository contains various scripts that introduce foundational concepts of the shell. Students will learn how to navigate directories, manage files, and perform basic operations.

## Requirements

- All scripts tested on Ubuntu 20.04 LTS
- Scripts are written in Bash 4.4 or later

## Installation

Clone this repository to your local machine to start working with the scripts:

```bash
git clone https://github.com/Omartalat/alx-system_engineering-devops.git
cd 0x00-shell_basics
```

## Usage

Each script can be executed to perform various tasks related to shell basics. Here's how you can make a script executable and run it:

```bash
chmod u+x script_name
./script_name
```

## Scripts Description

Here is a brief description of each script found in the repository:

1. **0-current_working_directory** - Prints the absolute path name of the current working directory.
2. **1-listit** - Displays the contents list of your current directory.
3. **2-bring_me_home** - Changes the working directory to the user’s home directory.
4. **3-listfiles** - Display current directory contents in a long format.
5. **4-listmorefiles** - Display current directory contents, including hidden files (starting with `.`).
6. **5-listfilesdigitonly** - Display current directory contents with user and group IDs displayed numerically.
7. **6-firstdirectory** - Create a directory named `my_first_directory` in the `/tmp/` directory.
8. **7-movethatfile** - Move the file `betty` from `/tmp/` to `/tmp/my_first_directory`.
9. **8-firstdelete** - Delete the file `betty`.
10. **9-firstdirdeletion** - Delete the directory `my_first_directory` that is in the `/tmp` directory.
11. **10-back** - Changes the working directory to the previous one.
12. **11-lists** - Lists all files (even ones with names beginning with a period character, which are hidden) in the current directory and the parent of the working directory and the `/boot` directory (in this order), in long format.
13. **12-file_type** - Prints the type of the file named `iamafile`.
14. **13-symbolic_link** - Create a symbolic link to `/bin/ls`, named `__ls__`.
15. **14-copy_html** - Copies all the HTML files from the current working directory to the parent of the working directory, but only copies files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

## Author

Omar Talat (@Omartalat)

## Acknowledgments

- Holberton School for providing the learning environment.
- Peers and mentors who provided guidance and support.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
