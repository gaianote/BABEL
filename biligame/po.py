import requests

def postbilibili(uname,upwd):
  payload = {'uname':uname,'upwd':upwd,'isused':False}
  requests.post('http://127.0.0.1:3000/api/bilibili',json=payload)
def getbilibilis():
  requests.get('http://127.0.0.1:3000/api/bilibilis')
def putbilibili():
  r = requests.get('http://127.0.0.1:3000/api/bilibili')
  data = r.json()
  print(data)
  id = data['bilibili']['id']
  payload = {'id':id}
  r = requests.put('http://127.0.0.1:3000/api/bilibili',json=payload)

class Bilan(object):
  def __init__(self):
    pass
  def post(self,uname,upwd,type):
    payload = {'uname':uname,'upwd':upwd,'type':type,'isused':False}
    requests.post('http://127.0.0.1:3000/api/bilan',json=payload)
  def get(self):
    r = requests.get('http://127.0.0.1:3000/api/bilan')
    print(r.json())
    return r.json()
  def getall(self):
    r = requests.get('http://127.0.0.1:3000/api/bilans',json=payload)
    return r.json()
  def put(self,data):
    r = requests.put('http://127.0.0.1:3000/api/bilan',json=data)


bilan = Bilan()
#data = bilan.post('12323123','322323','fdfddfdfd')
res = bilan.get()
bilan.put(res)
input()