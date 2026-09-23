# 基于网页版muv-luv girls garden的maze自动化脚本软件

## 目录

[TOC]

## 设计思路

通过对网页里面的`<canvas>`标签进行截图来实现图像识别, 然后通过图像识别功能操纵鼠标模拟人类进行自动化程序运行

## 所需要的功能

- 能够启动GUI
- 能够识别hwnd来寻找窗口
- 通过窗口进行截屏获取具体的画面
- 通过画面进行图像识别元素
- 能够操纵鼠标进行操作
- 能够实现界面状态机
- 能够在操作完成/操作出错/操作超时的时候提醒
- 拥有运行日志
- 最终形成一个可以长期运行的自动化程序
- 
## 主要流程

- 寻找标签
- 截图
- 判断目前状态
- 进入状态机
- 停止

## 核心设计/状态机设计

### 主界面状态机

- 开始界面
- 主界面
- 右下角的quest看不见
  - 寻找x号, 或者寻求帮助
  - 看得见, 下一步
- 点击quest
- 点击maze探索
  - 收取报酬
  - 无报酬直接进行下一步
- 选择设定难度
- 进入maze
- 自动化探索

### 自动化战斗状态机

- 有待研究

## 需要用到的技术

- 截图技术
- 图像识别技术
- 文字识别技术
- 鼠标模拟技术
- 窗口识别以及操纵技术

## 实用指令

进入虚拟环境

先进入项目根目录

``` cmd
.\.venv\Scripts\Activate.ps1
```

## 页面跳转数据

- navi
  - home
  - saakuru
  - quest
  - item
  - gacha
  - shop

- home
  - navi
  - presentBOX
  - mission
  - smart device
  - mine

- saakuru
  - navi
  - saakuru_misison
  - 交换所
  - saakuru_point收取

- quest
  - navi
  - mainquest
  - maze
  - part_simulation
  - exercises
  - activity

- shop
  - 期间限定
  - 交换所

- presentBOX
  - navi
  - present
  - worldPresent
  - back

