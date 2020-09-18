# chongli
chongli is an undetected reverse shell that doesn't need any ports open

# virus total
https://www.virustotal.com/gui/file/e4ec255546897648633ea4524bb3ef42c25dc7dc9b07941f221e5c7cb80ddb20/detection

note : windows only.

# usage

first you will need discord.py module which you can get by using pip

```
pip install discord.py
```

after that you will also need something to compile the code i recommend using pyinstalled 

```
pip install pyinstaller
```

now that you are all set go to discord developer portal create a bot and setup a server. 
copy the discord bot's token and put it in token variable and you are ready to compile the code

```
pyinstaller -F chongli.py
``` 

now just send the program to your target when they run it you get a very small but usable shell that can be used for foothold or anything else

happy hacking !(im not responsable for your actions btw)
