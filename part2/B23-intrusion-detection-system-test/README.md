# Activity B23 – Intrusion Detection System Test

## Objective
To test an intrusion detection system and discuss its effectiveness

## What I did
I made a simple IDS-style Python script that checks a login log for repeated failed login attempts.

## Findings
The script reads through a fake login log and counts how many failed login attempts come from each IP address.

I made it so if one IP address has 3 or more failed login attempts, the script prints an alert. This is because repeated failed logins can be a sign of someone trying to guess a password.

When I tested it, the script detected that 192.168.1.20 had 4 failed login attempts and flagged it as suspicious.

This is only a simple version of an IDS, but it shows the basic idea. A real intrusion detection system would look at more data and probably use more advanced rules, but this still shows how suspicious patterns can be detected.

## Evidence collected
I included the Python script, fake login log, and screenshots of the code and terminal output in the evidence folder.

## Reflection
This activity made me understand intrusion detection a bit better. Before doing this, I thought an IDS would be too complicated to test, but this showed me that the basic idea is just looking for suspicious behaviour or patterns.