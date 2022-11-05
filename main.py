import lightbulb

# Instantiate a Bot instance
bot = lightbulb.BotApp(token="MTAzNTE4MDIwMTgyODcwMDE2MA.GYxcQJ.YoAAlOzHEyKZ0AiVfXvp_tjH_gen62gDmsSUXM", prefix="$")

# Register the command to the bot
@bot.command
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "checks the bot is alive")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Pong!")

@bot.command
@lightbulb.command("hello", "hello")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("HELLO")

@bot.command
@lightbulb.command("instagram", " instagram link ")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("instagram : https://www.instagram.com/theprojectgrind/ ")

@bot.command
@lightbulb.command("youtube", " youtube link ")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("instagram : https://www.youtube.com/channel/UCHG5qAwYdc_SjIoBD5wpJYA")

bot.run()
