# Activity B25 – Threat Intelligence Module

## Objective
To design and implement a threat intelligence module of my choice

## What I did
I created a simple threat intelligence checker using Python.

## Findings
The module checks a domain name to see if it contains words that are commonly used in suspicious or fake domains.

I used words such as verify, account, password, secure, update, bank, payment, gift and prize.

The user enters a domain, and the program searches the domain for any of these suspicious words. If it finds any matches, it gives a warning and shows which words were found.

For example, a domain like secure-verification-update.com gets flagged because it contains words that are often used in phishing links.

A normal domain like google.com does not get flagged because it does not contain any of the suspicious words in the list.

This is a basic example of threat intelligence because it uses known indicators to help identify possible risks.

## Evidence collected
I included the Python file and screenshots showing the module being tested in the evidence folder.

## Reflection
This activity showed me how threat intelligence can be used to help identify suspicious domains. The tool is not perfect because real websites can also use some of these words, but it still shows how simple indicators can be used to flag something for further checking.