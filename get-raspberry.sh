#!/bin/bash

# Group File
FILE_GROUP=/home/lucacimini/exam-ig/$PI_HOST

# User File
FILE_USER=$FILE_GROUP/$PI_USERNAME

# Exam File
FILE_EXAM=/home/$PI_USERNAME/exam

# Creating User File on the local machine
if [ -e "$FILE_USER" ]
then
    echo "$FILE_USER exists."
    rm -rf "$FILE_USER"
    echo "Removed $FILE_USER."
    mkdir -p "$FILE_USER"
    echo "Created $FILE_USER."
else
    echo "$FILE_USER does not exists."
    mkdir -p "$FILE_USER"
    echo "Created $FILE_USER."
fi

# Importing Exam File from the remote machine
echo "Copying files..."
sshpass -p $PI_PASSWORD scp -o StrictHostKeyChecking=no -r $PI_USERNAME@$PI_HOST:$FILE_EXAM $FILE_USER
echo "Copy has finished."
