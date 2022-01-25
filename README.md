# CyberStartScripts
i delete my scripts too much
Sometimes i forget to indicate the level name, cyberstart puzzles locations might change from year to year.
Here's where i'll indicate them


l12c10.py = "Catch and Throw" - Read page 1, find and isolate number needed for timelock, use as cookie for requesting contents of site two. Poorly written, hard to read.
Bogdan.py = "Bogdan's Data"   - firstNum set to zero, secondNum set to firstNum so that secondNum = firstNum 100% of the time. I could've shrinked it more, but i did it in a rush. realised three months later that I could've just used netcat instead of making a script. MIGHT TAKE MULTIPLE TRIES. 
remote.py = "Remote Unlock"   - Get numbers, replace dots with spaces, split into three seperate strings, do the math, send back to server.
post.py =   "Account Roulette"- The output is not good for this one. Yes, it is supposed to look like that. Program curls with a user ID that increments by one each loop. Watch carefully for output.
l7c7DeveloperDisaster = "Developer Disaster" - Curls the URL with a UserID from 1-100. Gives immediate flag.
MBPsphrse.py = "Passphrase Panic - converts wordNumbers list to seperate int values, then creaes a list out of the randomwords file and selects the values given from wordNumbers. A bit messy and overcomplicated.
