# PasswordChecker
This is a program built to help you manage your own security. It will allow
you to check if any of your passwords have been in any security breach. It will use the pwnedpasswords.com site to help the search for any information and python to encrypt it.

Why do this program instead of just using the site? 
To answer this question we must understand we should not trust our information, specially our passwords to no one. Even though this website is secure and encrypted, you are still typing your password and running it through a server, a server wich can be breach with the correct ammount of work. With this password checker the only person or devices that will know your password, will be you and your machine. Your machine will encrypt/hash your password and after that will run it on the pwend website.

How it works and How to run?
You will have to run this program through your commandpromt, (every machine defers on how to type it, most common way is, cd inside the program folder and run 'pyhton checkpassword.py {password}' You can run any ammount of password at the time by separating them with a simple space. After typing the password, python will encrypt your password and will seek the 5 starting characters and will match them with a list of already leak passwords and on YOUR machine, no servers needed it will try and match the remaining characters with your encrypted password. If a match is found youll recieve a number. This number is number of databases that contain your password.

Remember, The best secrete is the one that is not told.
A.O.M



