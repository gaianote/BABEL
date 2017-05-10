import requests

class Bilibili(object):
  def __init__(self):
    pass
  def post(self,uname,upwd):
    payload = {'bilibili':{'uname':uname,'upwd':upwd,'isused':False}}
    return requests.post('http://127.0.0.1:3000/api/bilibili',json=payload)
  def get(self):
    return requests.get('http://127.0.0.1:3000/api/bilibili')
  def getall(self):
    return requests.get('http://127.0.0.1:3000/api/bilibilis')
  def put(self,data):
    return requests.put('http://127.0.0.1:3000/api/bilibili',json=data)

class Bilan(object):
  def __init__(self):
    pass
  def post(self,uname,upwd,type):
    payload = {'bilan':{'uname':uname,'upwd':upwd,'type':type,'isused':False}}
    return requests.post('http://127.0.0.1:3000/api/bilan',json=payload)
  def get(self):
    return requests.get('http://127.0.0.1:3000/api/bilan')
  def getall(self):
    return requests.get('http://127.0.0.1:3000/api/bilans')
  def put(self,data):
    return requests.put('http://127.0.0.1:3000/api/bilan',json=data)
