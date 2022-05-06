# echo-server-slash-commands
Discord bot that allows users to create private servers for echo with a slash command.

# How it works
I made the discord bot using py-cord due to the better support for slash commands. The main function is just one slash command that takes a location (like chicago, texas, etc...)
and a 'hold time' as the parameters. 

The bot will post a clickable link using the spark format (similar to... '<spark://c/7B800C25-2088-420F-A83C-B08D38EA6863>') a few seconds after the command is called

After the 'hold' time is passed the bot will leave the server.

# Slash command parameters
Location is fairly self-explanatory, in short it equates to what region arguement we pass in when opening the game.

Hold-time is the amount of time the bot 'holds' the server open, if no players join by the time the hold-time expires the server will be shut down and users will have to get a new one with a new slash command.

