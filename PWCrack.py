import argparse
import codecs
import sys
import os
import crypt
 
def passwordCrack(password, username):
   dictionary = open ('dictionary.txt','r')
   cryptfiend = password.split("$")[1]
   
   if cryptfiend == '6':
      saltygoodness = password.split("$")[2]
      totalsalt = "$" + cryptfiend + "$" + saltygoodness + "$"
      for line in dictionary.readlines():
         line = line.strip('\n')
         cryptLine = cryptfiend.crypt(line, totalsalt)
         
         if (cryptLine == password):
            print "Password is cracked dawg..." + username + line "\n"
            return
        else:
      print "Password not in dictionary..."
      exit
 
def parseLine():
   parser = argparse.ArgumentParser()
   args = parser.parse_args()
   
   if args.path == None:
      print "User does not exist or does not have a password..."
      exit
   
   else:
      passFile = open (args.path,'r')
         for line in passFile.readlines():
            line = line.replace("\n","").split(":")
            username = line[0]
            password = line[1]
            passwordCrack(password, username)

if __name__ == "__main__":
   parseLine()