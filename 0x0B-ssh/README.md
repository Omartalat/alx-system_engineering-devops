# 0x0B-ssh

## Description

This repository is part of the ALX Software Engineering program. The `0x0B-ssh` project focuses on understanding and applying the concepts of Secure Shell (SSH). Through this project, students will learn how to configure and secure SSH on a remote server, manage SSH keys, and use SSH for remote administration.

## Learning Objectives

- What is SSH
- What are servers and why do sysadmins need to use them
- What is a private/public key pair
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All your Bash script files must be executable
- Your Bash script must pass `shellcheck` without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

### Installation

SSH can be installed and configured on various types of servers, which often run Linux. For this project, we will focus on setting up SSH on Ubuntu.

1. Update your system:

   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. Install SSH:

   ```bash
   sudo apt install openssh-server
   ```

3. Check if SSH service is running:

   ```bash
   sudo systemctl status ssh
   ```

## Tasks

Here is a brief overview of the tasks involved in this project:

0. **Use a private key**
   - Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

1. **Create an SSH key pair**
   - A script to create an RSA key pair.

2. **Client configuration file**
   - An explanation on how to configure the `~/.ssh/config` to make logging into a server easier.

3. **Let me in!**
   - Add the SSH public key to a server to allow password-less entry.

4. **Client configuration file (advanced task)**
   - Enhance the configuration file to make it even more secure.

## Author

E-mail: <dr.omartalat@gmail.com>
Auther: @Omartalat

## Acknowledgements

This project is part of the curriculum of ALX. For further information, contact the ALX administration.
