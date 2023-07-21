# discord-bot
A discord bot that has 20+ commands.
# Discord Bot ReadME
## Introduction
This is a basic Discord bot created using Python and the discord.py library. The bot provides various fun and moderation commands to interact with users on Discord servers.

# Prerequisites
Python 3.x
```bash
discord.py library (install using pip install discord.py)
youtube_dl library (install using pip install youtube_dl) for music functionality (optional)
```
# Setup
Clone this repository to your local machine.
Obtain your Discord bot token from the Discord Developer Portal and replace 'YOUR_BOT_TOKEN' in bot.py with your token.
If you wish to use the music functionality, ensure you have installed the youtube_dl library.
Run the bot using python bot.py.

# Commands
The commands of this Bot.

```bash
!hello: The bot responds with a friendly greeting.
!ping: The bot responds with "Pong!" to check if it's online and responsive.
!info: Displays information about the bot, such as version, creator, etc.
!serverinfo: Shows information about the current Discord server.
!userinfo <mention>: Provides information about a user (or the message author if no mention).
!avatar <mention>: Shows the avatar of a user (or the message author if no mention).
!roll <num>: Rolls a random number between 1 and the specified number.
!coinflip: Flips a coin and returns "Heads" or "Tails".
!weather <location>: Retrieves the current weather for a given location (Uses OpenWeatherMap API).
Fun Image Commands
!cat: Sends a random cat picture.
!dog: Sends a random dog picture.
Music Commands (Optional)
!play <song>: Plays a song from YouTube or another platform in a voice channel.
!pause: Pauses the currently playing song.
!resume: Resumes the paused song.
!skip: Skips the current song and moves to the next one in the queue.
!stop: Stops the music and clears the queue.
Moderation Commands
!ban <user> <reason>: Bans a user from the server for a specified reason.
!kick <user> <reason>: Kicks a user from the server for a specified reason.
!mute <user> <time> <reason>: Mutes a user for the specified time with a reason.
!unmute <user>: Unmutes a previously muted user.
!warn <user> <reason>: Issues a warning to a user for a specified reason.
!clear <amount>: Deletes a specified number of messages from the current channel.
Reminder Command
!remindme <time> "<reminder>": Sets a reminder for the given time.
Contributing
Contributions to this Discord bot are welcome! Feel free to fork the repository and submit pull requests with your improvements or new features.
```
# License
This Discord bot is released under the MIT License.

