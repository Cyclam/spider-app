### 使用 pyenv 管理 python 版本
`curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash`

```shell
# Load pyenv automatically by adding
# the following to ~/.bash_profile:

export PATH="/Users/zeng/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv shell 3.5.4设置版本

[使用 pyenv 管理 Python 版本](http://einverne.github.io/post/2017/04/pyenv.html)
```

### 安装 Scrapy
1. `sudo pip install scrapy --upgrade --ignore-installed six`
2. 新建一个 scrapy 项目 `scrapy startproject project_name`

```
cd project_name
scrapy genspider example example.com
```

### Robot
- scrapy.cfg: 项目的配置文件。
- robot/: 该项目的python模块。之后您将在此加入代码。
- robot/items.py: 项目中的item文件。
- robot/pipelines.py: 项目中的pipelines文件。
- robot/settings.py: 项目的设置文件。
- robot/spiders/: 放置spider代码的目录。

`FEED_EXPORT_ENCODING = 'utf-8'` 在setting文件中设置处理unicode中文编码问题

### Spiders
- name: 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
- start_urls: 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取。
- parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的 Response 对象将会作为唯一的参数传递给该函数。 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的 Request 对象。

### Scapy 选择器
Scrapy使用css和xpath选择器来定位元素，它有四个基本方法：

1. xpath(): 返回选择器列表，每个选择器代表使用xpath语法选择的节点
2. css(): 返回选择器列表，每个选择器代表使用css语法选择的节点
3. extract(): 返回被选择元素的unicode字符串，要实际提取文本数据，必须调用选择器.extract()方法
4. re(): 返回通过正则表达式提取的unicode字符串列表

如果只想提取第一个匹配的元素，可以调用选择器 .extract_first()

### 开启爬虫
`scrapy crawl douban -o douban.csv`