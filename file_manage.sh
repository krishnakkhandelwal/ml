#!/bin/bash

# Step 1: Create directory and subdirectory
read -p "Enter directory name: " dirname
mkdir -p "$dirname"
echo "Directory '$dirname' created."

read -p "Enter subdirectory name: " subdirname
mkdir -p "$dirname/$subdirname"
echo "Subdirectory '$subdirname' created inside '$dirname'."

# Step 2: Create a .txt file using cat command
read -p "Enter file name (with .txt extension): " filename
echo "Enter file content (press Ctrl+D to save):"
cat > "$dirname/$filename"
echo "File '$filename' created."

# Step 3: Make a copy and rename it
read -p "Enter new file name for copy: " copyname
cp "$dirname/$filename" "$dirname/$copyname"
echo "File copied and renamed to '$copyname'."

# Step 4: Set permissions (rwx for owner, r-- for group/others)
chmod 744 "$dirname/$filename" "$dirname/$copyname"
echo "Permissions set: rwx for owner, r-- for group/others."

# Step 5: List files with permissions
echo "Listing files with permissions:"
ls -l "$dirname"

