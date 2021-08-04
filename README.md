# slack-user-bot
This python script allows users to use the Slack API to post messages in specific Slack channels on their behalf rather than a Slack Bot. Running this with Windows Task Scheduler or CRON can allow the user to send scheduled or recurring messages to a channel. 

To use this script, you must have python installed and have the slack module installed. (pip install slack)

1. Go to https://api.slack.com/ and create a new app.
2. Under the User Token Scopes section click 'Add an OAuth Scope' and type: chat:write
3. Click copy next to the User OAuth Token and paste it into the .env file in this directory.
4. In the Slack mobile or desktop application, add the newly created app to the channel you would like to post to from the channel settings.
5. To before running the python script, edit the slack-user-bot.py file and changing the token, channel, and message string variables. You can also use this by calling the send_message function from another file and passing the token, channel and message as string arguments.
