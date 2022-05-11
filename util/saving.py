def makeCommand(command,replywith):
  if command and replywith != None:
    if getLine(command) and getLine(command).rsplit("*!=")[0] == command:
      return False
    else:
      writeLine(f"{command} *!= {replywith}")

def getLine(get):
  with open('./data/commands.txt', 'r') as f:
      for line in f:
        if get in line:
          return line


def writeLine(text):
  f = open("./data/commands.txt","r+")

  content = f.read()

  if not content:
    f.write(text)
  else:
    f.write('\n' + text)