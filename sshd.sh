#! /bin/bash

if [[ $EUID -ne 0 ]]; then
echo "This script must be run as root"
   exit 2
read -r -p "Would you like to change the ssh port? [Y/N] " response
if [[ $response =~ ^([yY][eE][sS]|[yY])$ ]]
then
   read -p "What would you like to change the port? (choose between 1024-65535) " sshportconfig
   if (( ("$sshportconfig" > 1024) && ("$sshportconfig" < 65535) )); then
    echo "Port $sshportconfig" >> /etc/ssh/sshd_config
    echo "--------------------------------------------------------------------"
    echo "SSH port has been changed to: $sshportconfig. "
    echo "--------------------------------------------------------------------"
   else
    echo "Port chosen is incorrect."
    exit 1
   fi
else
   sshPort=$(grep "Port" /etc/ssh/sshd_config) | head -n 1
   echo "--------------------------------------------------------------------"
   echo "SSH is still: $sshPort"
   echo "---------------------------------------------------------------------"
   exit 1
fi
exit 0
#Bash file script
