def get_proxy_ip():
  # 文档 http://www.daxiangdaili.com/api
  import requests
  url = 'http://tvp.daxiangdaili.com/ip/'
  payload = {
  'tid': '558173393504430',
  'num': 1,
  'foreign':'none',
  'filter':'on',
  'category':2,
  'delay':1,
  'protocol':'https'
  }
  r = requests.get(url,params = payload)
  proxy_ip = r.text
  print(proxy_ip)
  return proxy_ip

def test():
  from selenium import webdriver
  chrome_options = webdriver.ChromeOptions()
  proxy_ip = get_proxy_ip()
  chrome_options.add_argument('--proxy-server=%s'%proxy_ip)
  chrome = webdriver.Chrome(chrome_options=chrome_options)
  #chrome.get('http://httpbin.org/ip')
  chrome.get('https://www.baidu.com')
  input()
  chrome.quit()
if __name__ == '__main__':
  test()