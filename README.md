# BUPT_ngwlogin
北京邮电大学ngw.bupt.edu.cn 校园网登录脚本

```bash
python ngw-login.py [[--user=2018xxxxxx] [--password=xxxxxx] [--line=CUC-BRAS] [--logout=True]]
```
--user        用户名
--password    密码
--line        线路
--logout      退出登录

##### 其实只需要一句:
```bash
curl 'http://10.3.8.211' --data "DDDDD=用户名&upass=密码&0MKKey="
```
就可以登录了，就把这个脚本当作学习python的例子吧😂
