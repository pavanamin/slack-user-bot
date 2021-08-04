import slack

token = "token" #User OAuth Token from Slack
message = 'message' #message to send to group
channel = 'channel' #channel to send message

def send_message(token, user_message, slack_channel):
        client = slack.WebClient(token)
        client.chat_postMessage(channel= slack_channel, text= user_message)
        print('The following message has been posted to the %s channel:', slack_channel)
        print(user_message)

send_message(token, message, channel)