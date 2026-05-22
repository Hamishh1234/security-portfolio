# Activity B17 – Implementing a State-of-the-Art Solution

## Objective
To implement and evaluate one current cybersecurity solution

## What I did
I made a basic file integrity monitoring tool using Python.

## Findings
File integrity monitoring is used in cybersecurity to check if important files have been changed.

For my version, I made a Python script that creates a SHA-256 hash of a file. A hash is like a unique fingerprint for the file. If the file changes, the hash should also change.

I tested this by running the script on a text file, then changing the text file and checking it again.

After I changed the file, the script detected that the hash was different and printed an alert saying the file had been changed.

This is only a simple version, but it shows the main idea behind file integrity monitoring. In real cybersecurity tools, this could be used to detect malware, tampering, or unauthorised changes to important files.

## Evidence collected
I included the Python script, the test text file, and screenshots showing the script detecting the file change in the evidence folder.

## Reflection
This activity helped me understand how file integrity monitoring works. Before doing this, I knew files could be checked for changes, but I did not really understand how hashing could be used to do it. It showed me that even a simple script can detect changes that might be important for security.