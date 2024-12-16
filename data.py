from twilio.rest import Client

account_sid = "AC71ee7178dc28f82faa6a4775cc6a94ba"
auth_token = "052a077d995aa178c146c2cd075a1b10"

client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+919573594554",
    body="it's going to rain today. remember to bring umbrella",
    from_="+919705644653")

print(message.sid)
