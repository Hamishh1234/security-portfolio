# Simple threat intelligence checker
# This checks if a domain contains words commonly used in fake or suspicious domains.

suspicious_words = [
    "verify",
    "verification",
    "secure",
    "security",
    "update",
    "account",
    "password",
    "reset",
    "bank",
    "payment",
    "support",
    "alert",
    "gift",
    "free",
    "win",
    "prize"
]

domain = input("Enter a domain to check: ").lower()

found_words = []

for word in suspicious_words:
    if word in domain:
        found_words.append(word)

if found_words:
    print("Warning: This domain contains suspicious words.")
    print("Matched words:", ", ".join(found_words))
else:
    print("No suspicious words found in the domain.")