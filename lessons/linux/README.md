# Linux
## Ubuntu
### Terminal
- Open explorer with command 
  - `nautilus --browser <PATH>`
- Open explorer in current dirctory using terminal
  - `xdg-open .`

### Keywords
- [ ] **cron** <sub>_Execute scheduled commands_</sub>
- [x] **clear** <sub>_Clear terminal_</sub>
- [x] **man** <sub>_Manual of command_</sub>
- [x] **df** <sub>_Disk space usage_</sub>
- Network
  - [x] **ping**
  - [x] **nslookup** <sub>_Query name servers_</sub>
  - [ ] **netstat** <sub>_Information about network_</sub>
    - `-p` | program, `-c` | continuous, `-a` | all, `-t` | tcp, `-u` | udp,`-l` | only listening sockets
    - [ ] `netstat -s` <sub>_Statistics for each protocol_</sub>
    - [ ] `netstat -i` <sub>_Table of all network interfaces_</sub>
    - [ ] `netstat -g` <sub>_Multicast group membership information for IPv4 and IPv6_</sub>
    - [ ] `netstat -r` <sub>_Kernel routing tables_</sub>
  - [ ] **netcat**
  - [ ] **ifconfig**
- File/Folder
  - [x] **dir** <sub>_List directory contents_</sub>
  - [x] **cd** <sub>_Change directory_</sub>
  - [x] **ls** <sub>_List all files and folders (Colorful)_</sub>
    - `ls -l` <sub>_With long, more detailed output_</sub>
    - `ls -a` <sub>_Including hidden files_</sub>
  - [x] **mkdir**
  - [x] **rmdir** <sub>_Remove directory_</sub>
  - [x] **rm**
  - [x] **mv**
  - [x] **cp**
  - [ ] **cut**
  - [x] **touch**
  - [ ] **locate** <sub>_Locate a file_</sub>
  - [ ] **ln** <sub>_Physical link between 2 files_</sub>
    - [ ] `ln -s` <sub>_Symbolic link between 2 files_</sub>
- [ ] **grep** <sub>_Search text in file_</sub>
- [ ] **sort**
- [ ] **wc** <sub>_Count words or chars in file_</sub>
- [ ] **dd**
- [ ] **traceroute**
- [ ] **vi**
- [ ] **chmod**
- [ ] **chown**
- [ ] **chgrp**
- [ ] **init**
- [ ] **kill**
- [ ] **gzip**
- [ ] **bzip2**
- [ ] **tar**
- [ ] **find**
- [ ] **wget**
- [ ] **chown**
- [ ] **su**
  - [ ] **sudo**
- [ ] **mount**
  - [ ] **umount**
- [ ] **fdisk**
- [ ] **nohup**
- [x] **whoami**
- [ ] **tail**
- [ ] **dpkg**
- [ ] **xargs**
- [x] **pwd** <sub>_Present working directory_</sub>
- [ ] **chroot**
- [ ] **tty**
- [ ] **fsck**
- [ ] **env**
- [x] **du** <sub>_Show disk usage_</sub>
- [ ] **dmesg**
- [ ] **useradd**
- [ ] **passwd**
- [x] **md5sum** <sub>_Check md5_</sub>
  - `md5sum file.ext`
    - This will return the md5 hash of that file
- [x] **sleep** <sub>_Delay_</sub>
  -  `sleep 10s`
- [ ] **tee**
- [ ] **modprobe**
- [x] **cat**
  - `cat file1.ext file2.ext`
    - To combine and show content of both
  - `cat>file.ext`
    - After this you can write text to file and exit with `CTRL+C`
- [ ] **echo** <sub>_Display text_</sub>
- [ ] **getopt** <sub>_Parse command options_</sub>