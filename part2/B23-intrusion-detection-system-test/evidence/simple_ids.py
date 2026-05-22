# Simple IDS test
# This checks a login log for repeated failed login attempts.

failed_attempts = {}

with open("login_log.txt", "r") as file:
    for line in file:
        line = line.strip()

        if "failed login from" in line:
            ip_address = line.split("from ")[1]

            if ip_address in failed_attempts:
                failed_attempts[ip_address] += 1
            else:
                failed_attempts[ip_address] = 1

print("IDS Scan Results:")

for ip, count in failed_attempts.items():
    if count >= 3:
        print("ALERT:", ip, "has", count, "failed login attempts")
    else:
        print(ip, "has", count, "failed login attempts")