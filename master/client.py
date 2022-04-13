import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections
import crypto
import crypto.Random
from crypto.Hash import SHA
from crypto.PublicKey import RSA
from crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self) -> None:
      random = crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self) -> binascii:
      return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
  value: float
  time: datetime
  def __init__(self, sender, recipient, value) -> None:
    self.sender = sender
    self.recipient = recipient
    self.value = value
    self.time = datetime.datetime.now()

  def to_dict(self) -> dict:
   if self.sender == "Genesis":
      identity = "Genesis"
   else:
      identity = self.sender.identity

   return collections.OrderedDict({
      'sender': identity,
      'recipient': self.recipient,
      'value': self.value,
      'time' : self.time})

  def sign_transaction(self) -> binascii:
   private_key = self.sender._private_key
   signer = PKCS1_v1_5.new(private_key)
   h = SHA.new(str(self.to_dict()).encode('utf8'))
   return binascii.hexlify(signer.sign(h)).decode('ascii')

  def display_transaction(Transaction):
   #for transaction in transactions:
   dict = Transaction.to_dict()
   send = str(dict['sender'])
   print ("sender: " + send)
   print ('-----')
   print ("recipient: " + dict['recipient'])
   print ('-----')
   print ("value: " + str(dict['value']))
   print ('-----')
   print ("time: " + str(dict['time']))
   print ('-----')

Dinesh = Client()
Ramesh = Client()
Seema = Client()
Vijay = Client()
transactions = []
t1 = Transaction(
   Dinesh,
   Ramesh.identity,
   15.0
)
t1.display_transaction()
print(t1.sign_transaction())
transactions.append(t1)