#!/usr/bin/python3
# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019/9/16 21:44
# @Author   : Raymond Luo
# @File     : config.py
# @User     : luoli
# @Software: PyCharm
# Reference:**********************************************
debug = False  # 在控制台显示log
wifi = "utsz"  # 选择您要自动登录的wifi，utsz 或者 hitsz
username = "***"  # 您的学号
passowrd = "***"  # 您的密码
check_time = 60 * 5  # 每隔多久检查是否断网，单位s
log = True  # 是否记录log
log_path = "./"  # log记录路径，默认为当前路径
retry = 3  # 设置登录失败重新连接次数