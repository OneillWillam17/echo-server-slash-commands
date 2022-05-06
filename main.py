import asyncio
import time
from dotenv import load_dotenv
import os
import discord
from discord.commands import Option
from echo import Echo

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = discord.Bot()
echo = Echo()


# makes sure that the bot is fully ready before accepting any slash commands
@bot.event
async def on_ready():
    print(f"logged in as {bot.user}")


@bot.slash_command()
async def pull_server(ctx,
                      location=Option(str,
                                      description="Choose location of server, options are in the bot's description",
                                      required=True),
                      hold_time=Option(int,
                                       description="How long should the bot stay in the server?, max of 300 seconds",
                                       required=False,
                                       default=120,
                                       min_value=60,
                                       max_value=300)
                      ):

    # type hints to make using some methods easier later in the function
    hold_time: int
    location: str

    try:
        hold_time = int(hold_time)
    except TypeError:
        # user didn't define a set amount of seconds
        hold_time = 120

    location = location.strip().lower()

    if hold_time > 300:
        await ctx.respond("Cannot hold server for more than 300 seconds at a time")
    else:
        if location not in echo.server_dict.keys():
            await ctx.respond(f"Invalid server location, valid locations are {', '.join(list(echo.server_dict.keys()))}")
        else:
            echo.open_temp_server(location=echo.server_dict[location])
            await ctx.respond(f"Opening {location} server...")
            # sleep to allow server to spin up and give local api access
            await asyncio.sleep(45)
            await ctx.send(echo.create_spark_link())
            # hold time is there to allow the players to get into the lobby themselves
            # means the bot doesn't have to stay there forever and allow it to create other servers
            time.sleep(hold_time)
            os.system("TASKKILL /F /IM echovr.exe")  # closes echovr.exe


bot.run(token)
