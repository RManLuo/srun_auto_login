<h1 align="center">Welcome to srun_auto_login 👋</h1>
<p>
  <a href="https://mit-license.org/">
    <img alt="License: MIT License" src="https://img.shields.io/badge/License-MIT License-yellow.svg" target="_blank" />
  </a>
</p>

> 深澜校园网自动后台常驻保证在线，支持windows、linux、mac，妈妈再也不用担心电脑被挤掉线了。

## Requirements

```sh
selenium >= 3.141.0
```

## Usage
在config.py文件中输入您的账户和密码，然后愉快的开始运行吧。

### WIndows后台运行
```sh
pythonw auto_login.py
```
### Mac and Linux后台运行
```sh
nohup python3 auto_login.py 2>&1 &
```
## 通过bat注册windows开机自启
1.将auto_login.py 改名成auto_login.pyw，并右键创建快捷方式
2.点击开始--所有程序--启动--右击--打开，将已快捷方式复制到该目录（C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup）下，可能杀毒软件会阻止，选择允许，然后重启电脑即可。
## Author

👤 **Raymond Luo**

* Github: [@RManOfCN](https://github.com/RManOfCN)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Raymond Luo](https://github.com/RManOfCN).<br />
This project is [MIT License](https://mit-license.org/) licensed.

***
_This README was generated with ❤️ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
