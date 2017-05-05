import rem
import time
import datetime

# 保存日志
def savelog(ad):
  now = datetime.datetime.now()
  now = now.strftime('%Y-%m-%d %H:%M:%S')
  info = now + ' 点击成功: ' + ad.text + '\n'
  print(info)
  with open('task.log', 'a+',encoding='UTF-8') as f:
      f.write(info)

# 点击广告
def clickads (keyword,white_list):
  claw = rem.Claw()
  claw.fake('pc')
  claw.wait(20)
  try:
    claw.get('https://www.baidu.com')
    if not claw.query('#kw'):
      claw.driver.quit()
  except Exception as e:
    claw.driver.quit()
    return False
  claw.query('#kw').send_keys(keyword)
  claw.query('#su').click()
  claw.query('h3.t')
  js = '''
  const getads = (white_list) => {
    let titles = document.querySelectorAll('h3.t')
    let ads = []
    for(title of titles){
      if(title.classList.length === 3){
        console.log(title)
        let url = title.querySelector('a').getAttribute('data-landurl')
        is_click = true;
        for(site of white_list){
          if(url.search(site) !== -1){
            is_click = false
          }
        }
        if(is_click){
          ads.push(title.querySelector('a'))
        }
      }
    }
    return ads
  }
  return getads(%s)
  '''%white_list
  ads = claw.run_js(js)
  for ad in ads:
    ad.click()
    savelog(ad)
  time.sleep(20)
  claw.driver.quit()

# 启动程序
def main(keywords,white_list):
  while True:
    for keyword in keywords:
      try:
        clickads(keyword,white_list)
      except Exception as e:
        pass


################################################################################################
keywords = ['1553b']
white_list = ['taobao','1688','horntech']

main(keywords,white_list)

