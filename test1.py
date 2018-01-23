from dealerclient.api import client

# Init session
ses = client.create_session(token='token') # Pick up default base_url
# Or, use username and password
# ses = client.create_session(username='username', password='password') # Pick up default base_url

dealer = client.Client(session=ses) # Pick up default dealer_url

workspaces = dealer.workspaces.list()
# Print all workspace names
print([w.Name for w in workspaces])