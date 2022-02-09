'''
python program for getting the word count from a text.
Developed by: SRIJITH R
RegisterNumber: 21004191
'''
def wordcount(filen):
  count = 0
  with open(filen,"r") as f1:
    data=f1.read()
    for line in data.split():
      count += 1
  print("The word count is", count)
filename=input("Enter Filename:")
wordcount(filename)