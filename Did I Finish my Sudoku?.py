def done_or_not(board): #board[i][j]
  # your solution here
  somai = 0
  somaj = 0
  somar = 0
  for x in range (0,9,1):
      for y in range (0,9,1):
          somaj += board[x][y]
      if somaj == 45:
          somaj = 0
      else: return 'Try again!'
  for y in range (0,9,1):
      for x in range (0,9,1):
          somai += board[x][y]
      if somai == 45:
          somai = 0
      else: return 'Try again!'
  for x in range (0,3,1):
      for y in range(0,3,1):
          somar += board[x][y]
  print(somar)
  if somar == 45:
      somar = 0
  else: return 'Try again!'
  for x in range (3,6,1):
      for y in range(3,6,1):
          somar += board[x][y]
  if somar == 45:
      somar = 0
  else: return 'Try again!'
  for x in range (6,9,1):
      for y in range(6,9,1):
          somar += board[x][y]
  if somar == 45:
      somar = 0
  else: return 'Try again!'
  return 'Finished!'
  