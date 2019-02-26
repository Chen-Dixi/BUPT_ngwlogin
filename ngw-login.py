import requests
from absl import flags
from absl import app
from bs4 import BeautifulSoup
import os
from functools import partial
FLAGS = flags.FLAGS

flags.DEFINE_string('user','2018xxxxxx','username of your campus account')
flags.DEFINE_string('password','xxxxxx','password of your campus account')
flags.DEFINE_string('line','CUC-BRAS','which line do you prefer')
flags.DEFINE_boolean('logout',False,'set true if you want to logout')
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,de;q=0.7,pt;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin':'http://ngw.bupt.edu.cn',
    'Referer':'http://ngw.bupt.edu.cn.index',
    'Upgrade-Insecure-Requests':'1',
}


class NgwLoginTool(object):
    def __init__(self,username,password,line,http_timeout):
        self._session = requests.Session()
        self._get = partial(self._session.get, headers=HEADERS,timeout=http_timeout)
        self._post = partial(self._session.post, headers=HEADERS, timeout=http_timeout)
        self.username = username
        self.password = password
        self.line = line
    def _login(self):
        login_url = 'http://ngw.bupt.edu.cn/login'
        auth_data = {
            'user':self.username,
            'pass':self.password,
            'line':self.line,
        }
        response = self._post(login_url,auth_data)
        response.encoding = 'utf-8'
        text = response.text
        soup = BeautifulSoup(text,'html.parser')
        h3 = soup.find_all('h3')[0]
        if h3.text == '登录成功':
                print('账号'+self.username+'登录成功\n')
    def _logout(self):
        logout_url='http://ngw.bupt.edu.cn/logout'
        self._get(logout_url)
        print("已登出")

def main(argv):
    if FLAGS.user is not None and FLAGS.password is not None and FLAGS.line is not None:
        loginTool = NgwLoginTool(FLAGS.user,FLAGS.password,FLAGS.line,15)
        if FLAGS.logout:
            loginTool._logout()
        else:
            loginTool._login()


if __name__ == '__main__':
    app.run(main)


