def getToken():
  f = open("token.txt","r")
  return f.read()

def setToken(token):
  f = open("token.txt", "x")
  f = open("token.txt","w")
  print(f"Sat your token to {token}")
  f.write(token)