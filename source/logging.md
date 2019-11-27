


> Written with [StackEdit](https://stackedit.io/).

#  logging


##  简介


日志就是追踪在软件运行时产生的事件的方法. 一般由该软件的开发人员将日志记录调用添加到其代码中, 以指示已发生某些事件. 

对于我们公司来说, 开发借助日志进行调试, 测试使用日志校验逻辑和功能, 运维监控日志提供预警, 数据依赖日志分析行为偏好.

因此, 日志记录是非常有必要的. 作为开发者, 我们需要重视并做好日志记录过程.


##  logging 及其组件

在 Python 中有一个标准的 logging 模块，我们可以使用它来进行标注的日志记录，利用它我们可以更方便地进行日志记录，同时还可以做更方便的级别区分以及一些额外日志信息的记录，如时间、运行模块信息等。

 -  Loggers
 -  Filters
 -  Handlers
 -  Formatters
 -  LogRecord

组件交互图:

![enter image description here](https://docs.python.org/3/_images/logging_flow.png)



###  Logger

Logger 是用来执行日志流程的主类. 日志内容的产生, 转化, 过滤在此进行.
Logger 默认是一个树型的继承体系. 默认就是的 logger 又叫做 root logger.
其他的 logger 均继承此 root logger.  Logger 的层级通过 "." 来进行区分

如下, spam 是 spam.foo 的父 logger, 而 spam.foo 是 spam.foo.bar 的父 logger.
(可以理解为一颗前缀树)
```python
spam=logging.getLogger("spam")
spam_foo=logging.getLogger("spam.foo")
spam_foo_bar=logging.getLogger("spam.foo.bar")

spam_foo_bar.info("the message 1")
spam.info("the message 2")
``` 

#### 层级

Logger 只负责生成日志内容, 并传递至父类的各级 Logger 中.
以上面的代码举例子, 

 1. "the message 1" 会在四个 Logger 都生成一个消息记录(LogRecord).
 2. "the message 2" 会在两个 Logger 都生成一个消息记录(LogRecord).

如果要阻止向父类 Logger 传递日志内容,  请把 **propagate** 属性置为 False.

#### level
Logger 会过滤掉小于当前等级的日志内容. 默认是日志级别是  **WARNING**.

| Level      | Numeric value |
|------------|---------------|
| `CRITICAL` |       50      |
| `ERROR`    |       40      |
| `WARNING`  |       30      |
| `INFO`     |       20      |
| `DEBUG`    |       10      |
| `NOTSET`   |      0        |




###  Handlers

**Logger** 负责日志的产生, 而日志的最终输出就由 **Handlers** 负责进行.
下面是输出到文件的例子: 

```python
import logging 
logger = logging.getLogger("example")
logger.setLevel(level=logging.INFO) 
handler = logging.FileHandler('example.log') 
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.info('info logs') 
logger.debug('debugging logs') 
logger.warning('warning logs')
logger.info('final info logs')
```

```shell
#日志输出

2019-11-26 16:39:35,005 - example - INFO - info logs
2019-11-26 16:39:35,005 - example - WARNING - warning logs
2019-11-26 16:39:35,005 - example - INFO - final info logs
```

logging:
 - StreamHandler: 日志输出流, 可以到标准输出(/dev/stdout), 标准错误输出(/dev/stderr)
 - FileHandler: 如上所示, 日志输出到文件.
 - [`NullHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler "logging.NullHandler") : 空Handler, 只记录日志, 不输出日志.

logging.handlers
 - RotatingHandler: 按大小转储日志文件.
 - TimeRotatingHandler: 按时间周期转储日志文件.
 - SysLogHandler: 把日志输出到 syslog.
 - SMTPHandler: 把日志输出至指定邮件地址.
 - HTTPHandler: 通过 HTTP 协议输出日志.

除了这些常用的 Handler, 还有基于 TCP, UDP 的, 以及基于不同组件输出日志.
继承基类 Handler, 还可以实现更多的定制化的Handler, 比如你可以实现一个Handler 直接把日志输出至 kafka, 或者数据库等.

###  Formatters &&  LogRecord

控制日志的输出目的地是 **Handler**, 输出的格式就由  Formatters 指定.
上面例子中的格式如下:

```python
# Format:
'%(asctime)s - %(name)s - %(levelname)s - %(message)s'
```
结果日志输出如下:
```shell
2019-11-26 16:39:35,005 - example - INFO - info logs
2019-11-26 16:39:35,005 - example - WARNING - warning logs
2019-11-26 16:39:35,005 - example - INFO - final info logs
```
%(asctime)s      输出本地时间
%(name)s          输出logger的名字
%(levelname)s  输出日志的级别
%(message)s     输出实际的日志内容

Format 和 LogRecord 的属性(Attribute)是一一对应的.
请参考: [https://docs.python.org/3/library/logging.html#logrecord-attributes](https://docs.python.org/3/library/logging.html#logrecord-attributes)


##  best practice


###  使用 logging 替代 print

很多人习惯在开发时使用 print 替代日志, 然后再代码发布时移除这些 print 语句.
随着代码层级的加深和逻辑的复杂, 使用 print 很难满足多变的日志格式的需求,
甚至你可能忘了去掉这些 print 语句. 各种信息混在一起, 使得日志的排查愈加困难.

###  日志是单实例的

同一个 Logger 在不同模块获得都是一个实例. 如下所示:

```python
spam=logging.getLogger("spam")
```
如果在 a, b 模块都是用此语句获得 spam Logger, 则这是同一个实例.


###   在日志中记录相关异常栈

把异常栈记录到日志中:

```python
import logging
import traceback
try:
  c = 7 / 0
except Exception as e:
    logging.error("Exception occurred:%s", traceback.format_exc())
```

请使用 pythonic 的做法:
```python

import logging
try:
  c = 7 / 0
except Exception as e:
  logging.error("Exception occurred", exc_info=True)
```


###  线上环境使用日志转储

在生产环境中, 程序会一直产生日志, 为了防止磁盘被日志文件占满. 可以按照文件大小转储或时间转储日志文件, 这样可以节省维护的压力.

###  使用合理的日志级别
合理安排输出日志的级别,  避免日志洪流. 尽可能思考输出不同等级的日志.
便于后期不同需求的人来排查逻辑.

###  库程序使用 NullHandler

如果是提供别人使用的程序库, 一般会把 warnning 信息输出到 stderr(标准错误输出).  但是如果应用的标准错误输出有其他的用途, 不希望任何引用的第三方库把日志输出到标准错误输出时或者输出到其他的任何输出位置, 那么可以使用一个占位符的"空"Handler, 它接收到日志后什么也不做.
如下所示,
```python
# foo.py
import logging
logging.getLogger('foo').addHandler(logging.NullHandler())
```
参考:[https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library](https://docs.python.org/3/howto/logging.html#configuring-logging-for-a-library)

It is strongly advised that you _do not add any handlers other than_  [`NullHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.NullHandler "logging.NullHandler")  _to your library’s loggers_. This is because the configuration of handlers is the prerogative of the application developer who uses your library. The application developer knows their target audience and what handlers are most appropriate for their application: if you add handlers ‘under the hood’, you might well interfere with their ability to carry out unit tests and deliver logs which suit their requirements.

###   Use __name__ as the logger name
这样可以使得 Logger 的名字和模块的名字统一. 可以用 Formatters 在日志中显示记录日志的模块, 行号. 便于定位程序逻辑的位置.
并且如上面的例子所示, 恰好也满足日志的继承层级, 
```python
spam_foo=logging.getLogger("spam.foo")
```
这样可以只给父类 Logger 设置 Handler, 那么模块中所有子子模块输出的日志都能输出.



###  多进程写日志

因为我们的线上服务 tornado 使用多进程启动. 一旦在开始时配置了日志,
又使用日志大小转储. 那么多个进程就会往一个日志文件里面写日志. 直到
某一个进程写入一个新的日志记录时发现需要转储, 它便转储当前日志文件,
并重新创建一个新的日志文件. 但是其他进程并不知道, 仍然维持之前被重命名转储的那个文件(linux中不是靠文件名来识别文件, 而是文件句柄, 一个数字).当另一个进程也写一条日志时, 发现也需要转储, 会重新转储当前日志, 并重新写新的日志.结果就是会导致日志的混乱.


#### 单进程写日志
代码如下:

```python
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
rotate_hd = RotatingFileHandler(filename="/tmp/whtest/test.log",
                                maxBytes=1*1024, backupCount=2)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(process)d - %(message)s')
rotate_hd.setFormatter(f_format)
logging.basicConfig(handlers=[rotate_hd], level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
pid = os.getpid()
for i in range(100):
    logging.info("info message")
```

结果如下:

```shell
ryefccd@fccd:/tmp/whtest$ ll
总用量 152
drwxrwxr-x  2 ryefccd ryefccd   4096 11月 27 12:10 ./
drwxrwxrwt 15 root    root    135168 11月 27 12:09 ../
-rw-rw-r--  1 ryefccd ryefccd    990 11月 27 12:10 test.log
-rw-rw-r--  1 ryefccd ryefccd    990 11月 27 12:10 test.log.1
-rw-rw-r--  1 ryefccd ryefccd    990 11月 27 12:10 test.log.2

```

####  多进程写日志

代码如下:
```python
import os
import sys
import logging
from logging.handlers import RotatingFileHandler
rotate_hd = RotatingFileHandler(filename="/tmp/whtest/test.log",
                                maxBytes=1*1024, backupCount=2)
f_format = logging.Formatter('%(asctime)s - %(name)s - %(process)d - %(message)s')
rotate_hd.setFormatter(f_format)
logging.basicConfig(handlers=[rotate_hd], level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# pid = os.getpid()
for _ in range(3):
    pid = os.fork()
for i in range(100):
    logging.info("info message")
```

结果如下:

```shell
--- Logging error ---
Traceback (most recent call last):
  File "/home/ryefccd/python3.5/python3.5.2/lib/python3.5/logging/handlers.py", line 72, in emit
    self.doRollover()
  File "/home/ryefccd/python3.5/python3.5.2/lib/python3.5/logging/handlers.py", line 169, in doRollover
    os.rename(sfn, dfn)
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/whtest/test.log.1' -> '/tmp/whtest/test.log.2'
Call stack:
  File "logging_test.py", line 21, in <module>
    logging.info("info message")
Message: 'info message'
Arguments: ()
ryefccd@fccd:/tmp/whtest$ ll
总用量 152
drwxrwxr-x  2 ryefccd ryefccd   4096 11月 27 12:20 ./
drwxrwxrwt 15 root    root    135168 11月 27 12:19 ../
-rw-rw-r--  1 ryefccd ryefccd    540 11月 27 12:20 test.log
-rw-rw-r--  1 ryefccd ryefccd    972 11月 27 12:20 test.log.1
-rw-rw-r--  1 ryefccd ryefccd    540 11月 27 12:20 test.log.2
```


####  最终方案

 1. 最简单, 也是最直接可靠的办法就是一个进程写一个日志.
在fork之后初始化日志并更根据进程号写不同的日志文件.
 2. RotatingFileHandler 进行转储时不仅判断大小还要判断当前的文件名.
优先判断当前文件的文件名, 如果不是原始的文件名, 则修改为往最开始的文件名中写入日志.(没来得及做)
3. [https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes](https://docs.python.org/3/howto/logging-cookbook.html#logging-to-a-single-file-from-multiple-processes)




##  引用

[Logging HOWTO](https://docs.python.org/3/howto/logging.html)
[Logging in Python](https://realpython.com/python-logging/)
