from aqua import Aqua


aqua = Aqua(id='username', password='password', host='192.0.2.8', port='443', using_ssl=True)
print(aqua.token)