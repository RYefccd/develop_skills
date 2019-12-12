


> Written with [StackEdit](https://stackedit.io/).

#  debug

##  pdb(ipdb)

###  demo

 - start.py
```python

import foo
import bar

tmp1 = "123"
tmp2 = "3f6"

print("tmp1 is num: %s by foo.is_num func" % foo.is_num(tmp1))
print("tmp2 is num: %s by foo.is_num func" % foo.is_num(tmp2))

print("tmp1 is num: %s by bar.is_num func" % bar.is_num(tmp1))
print("tmp2 is num: %s by bar.is_num func" % bar.is_num(tmp2))
```

 - foo.py

```python
def is_num(x):
    flag = x.isnumeric()
    return flag
```

 - bar.py

```python
def is_num(x):
    start = ord('0')
    end = ord('9')
    flag = True
    for i in x:
        num = ord(i)
        if not start <= num <= end:
            flag = False
            break
    return flag
```


###  introduction

 - 进入调试的两种方法
1.
```python
import pdb; pdb.set_trace()
```
2.
```shell
python -m pdb start.py
```

 - use ipdb

```shell
pip install ipdb
python -m ipdb start.py
```
 - printing expressions

```python
> /home/ryefccd/env/server18/debug/start.py(6)<module>()
      5 tmp1 = "123"
----> 6 tmp2 = "3f6"
      7 

ipdb> p tmp1                                                                                                                                                                                                 
'123'
ipdb> p tmp2                                                                                                                                                                                                 
*** NameError: name 'tmp2' is not defined

```

 - stepping through code with `n` (next) and `s` (step)
```python
ipdb> ll                                                                                                                                                                                                     
      1 
      2 import foo
      3 import bar
      4 
      5 tmp1 = "123"
      6 tmp2 = "3f6"
      7 
----> 8 print("tmp1 is num: %s by foo.is_num func" % foo.is_num(tmp1))
      9 print("tmp2 is num: %s by foo.is_num func" % foo.is_num(tmp2))
     10 
     11 print("tmp1 is num: %s by bar.is_num func" % bar.is_num(tmp1))
     12 print("tmp2 is num: %s by bar.is_num func" % bar.is_num(tmp2))

ipdb> n                                                                                                                                                                                                      
tmp1 is num: %s by foo.is_num func True
> /home/ryefccd/env/server18/debug/start.py(9)<module>()
      8 print("tmp1 is num: %s by foo.is_num func" % foo.is_num(tmp1))
----> 9 print("tmp2 is num: %s by foo.is_num func" % foo.is_num(tmp2))
     10 

ipdb> s                                                                                                                                                                                                      
--Call--
> /home/ryefccd/env/server18/debug/foo.py(1)is_num()
----> 1 def is_num(x):
      2     flag = x.isnumeric()
      3     return flag

```

 - using breakpoints
```python
ipdb> w                                                                                                                                                                                                      
  /home/ryefccd/python3.5/python3.5.2/lib/python3.5/bdb.py(431)run()
    430         try:
--> 431             exec(cmd, globals, locals)
    432         except BdbQuit:

  <string>(1)<module>()

> /home/ryefccd/env/server18/debug/start.py(11)<module>()
     10 
---> 11 print("tmp1 is num: %s by bar.is_num func" % bar.is_num(tmp1))
     12 print("tmp2 is num: %s by bar.is_num func" % bar.is_num(tmp2))

ipdb> ll                                                                                                                                                                                                     
      ...
      8 print("tmp1 is num: %s by foo.is_num func" % foo.is_num(tmp1))
      9 print("tmp2 is num: %s by foo.is_num func" % foo.is_num(tmp2))
     10 
---> 11 print("tmp1 is num: %s by bar.is_num func" % bar.is_num(tmp1))
     12 print("tmp2 is num: %s by bar.is_num func" % bar.is_num(tmp2))


ipdb> b bar:3                                                                                                                                                                                                
Breakpoint 1 at /home/ryefccd/env/server18/debug/bar.py:3
ipdb> c                                                                                                                                                                                                      
> /home/ryefccd/env/server18/debug/bar.py(3)is_num()
      2     start = ord('0')
1---> 3     end = ord('9')
      4     flag = True

```

 - continuing execution with `unt` (until)
```python
ipdb> ll                                                                                                                                                                                                     
      1 def is_num(x):
      2     start = ord('0')
1---> 3     end = ord('9')
      4     flag = True
      5     for i in x:
      6         num = ord(i)
      7         if not start <= num <= end:
      8             flag = False
      9             break
     10     return flag

ipdb> l                                                                                                                                                                                                      

ipdb> unt 8                                                                                                                                                                                                  
> /home/ryefccd/env/server18/debug/bar.py(10)is_num()
      8             flag = False
      9             break
---> 10     return flag

ipdb> p flag                                                                                                                                                                                                 
True
```
 - displaying expressions

```python
> /home/ryefccd/env/server18/debug/bar.py(3)is_num()
      2     start = ord('0')
1---> 3     end = ord('9')
      4     flag = True

ipdb> ll                                                                                                                                                                                                     
      1 def is_num(x):
      2     start = ord('0')
1---> 3     end = ord('9')
      4     flag = True
      5     for i in x:
      6         num = ord(i)
      7         if not start <= num <= end:
      8             flag = False
      9             break
     10     return flag

ipdb> display i, num                                                                                                                                                                                         
display i, num: ** raised NameError: name 'i' is not defined **
ipdb> b 7                                                                                                                                                                                                    
Breakpoint 2 at /home/ryefccd/env/server18/debug/bar.py:7
ipdb> b                                                                                                                                                                                                      
Num Type         Disp Enb   Where
1   breakpoint   keep yes   at /home/ryefccd/env/server18/debug/bar.py:3
	breakpoint already hit 1 time
2   breakpoint   keep yes   at /home/ryefccd/env/server18/debug/bar.py:7
ipdb> c                                                                                                                                                                                                      
> /home/ryefccd/env/server18/debug/bar.py(7)is_num()
      6         num = ord(i)
2---> 7         if not start <= num <= end:
      8             flag = False

display i, num: ('1', 49)  [old: ** raised NameError: name 'i' is not defined **]
ipdb> c                                                                                                                                                                                                      
> /home/ryefccd/env/server18/debug/bar.py(7)is_num()
      6         num = ord(i)
2---> 7         if not start <= num <= end:
      8             flag = False

display i, num: ('2', 50)  [old: ('1', 49)]
ipdb> c                                                                                                                                                                                                      
> /home/ryefccd/env/server18/debug/bar.py(7)is_num()
      6         num = ord(i)
2---> 7         if not start <= num <= end:
      8             flag = False

display i, num: ('3', 51)  [old: ('2', 50)]
```

 - finding the caller of a function(where)

```python
ipdb> w                                                                                                                                                                                                      
  /home/ryefccd/python3.5/python3.5.2/lib/python3.5/bdb.py(431)run()
    430         try:
--> 431             exec(cmd, globals, locals)
    432         except BdbQuit:

  <string>(1)<module>()

  /home/ryefccd/env/server18/debug/start.py(11)<module>()
     10 
---> 11 print("tmp1 is num: %s by bar.is_num func" % bar.is_num(tmp1))
     12 print("tmp2 is num: %s by bar.is_num func" % bar.is_num(tmp2))

> /home/ryefccd/env/server18/debug/bar.py(7)is_num()
      6         num = ord(i)
2---> 7         if not start <= num <= end:
      8             flag = False
```


###  cheatsheet
帮助

 - Use **h**(elp) or ? to list all commands.

控制
 - **n**(ext) -> Continue execution until the next line in the current function is reached or it returns.
 - **s**(tep) -> Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).
 - **r**(eturn) -> Continue execution until the current function returns.
 - **u**( p) and **d**(own) -> Move the current frame count (default one) levels up/down in the stack trace (to an older/newer frame).
 - **c**(ont(inue)) can be useful if you have multiple breakpoints, it continues execution until a next breakpoint is encountered.
 - **unt**(il) [lineno] -> Without argument, continue execution until the line with a number greater than the current one is reached. -> useful to get out of a for loop.
 - **b**(reak) [lineno] and **cl**(ear) to set / clear a break point in the current file (it even accepts a condition).

打印上下文

 - **l**(ist) -> List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing.
 - **w**(here) -> Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands. -> handy for web frameworks
 - **bt** -> Get a stack trace of the functions that have been called so far.
 - **pp** expression -> Like the p command, except the value of the expression is pretty-printed using the pprint module -> very useful for nested data structures.

###  相比 gdb 的缺陷

不能附加在一个已经开始运行的进程中.

###  参考资料

[https://realpython.com/python-debugging-pdb/#displaying-expressions](https://realpython.com/python-debugging-pdb/#displaying-expressions)

##  gdb

gdb 是 gnu 自由软件维护的一个调试工具. 支持多种语言的调试.


### 使用场景

There are types of bugs that are difficult to debug from within Python:

-   segfaults (not uncaught Python exceptions)
-   hung processes (in cases where you can't get a Python traceback or debug with  pdb)
-   out of control daemon processes

###  安装

 - ubuntu

```shell
sudo apt-get install gdb python3-dbg
```

 - centos

```shell
sudo yum install gdb python-debuginfo
```


###  使用

实际情况中, 一般是在上面所说的异常时通过下面的命令进入进程.

```
gdb python3 -p  进程号
```
注意, 这个 python 一定是要上面装了调试信息的那个Python解释器.


首先开启进程
```shell
ryefccd@fccd:~/env/server18/debug$ python3.4 start.py 
tmp1 is num: True by foo.is_num func
tmp2 is num: False by foo.is_num func

```

然后附加到进程进行调试
```shell
ryefccd@fccd:~/env/server18/debug$ ps -ef f|grep python3.4
ryefccd  18600 17607  0 17:02 pts/39   S+     0:00          |   |   \_ grep --color=auto python3.4
ryefccd  18477 24591  0 17:01 pts/41   S+     0:00          |       \_ python3.4 start.py
ryefccd@fccd:~/env/server18/debug$ sudo gdb  python3.4 -p  18477
GNU gdb (Ubuntu 7.7.1-0ubuntu5~14.04.3) 7.7.1
Copyright (C) 2014 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from python3.4...Reading symbols from /usr/lib/debug//usr/bin/python3.4m...done.
done.
Attaching to program: /usr/bin/python3.4, process 18477
Reading symbols from /lib/x86_64-linux-gnu/libpthread.so.0...Reading symbols from /usr/lib/debug//lib/x86_64-linux-gnu/libpthread-2.19.so...done.
done.
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
Loaded symbols for /lib/x86_64-linux-gnu/libpthread.so.0
Reading symbols from /lib/x86_64-linux-gnu/libc.so.6...Reading symbols from /usr/lib/debug//lib/x86_64-linux-gnu/libc-2.19.so...done.
done.
Loaded symbols for /lib/x86_64-linux-gnu/libc.so.6
Reading symbols from /lib/x86_64-linux-gnu/libdl.so.2...Reading symbols from /usr/lib/debug//lib/x86_64-linux-gnu/libdl-2.19.so...done.
done.
Loaded symbols for /lib/x86_64-linux-gnu/libdl.so.2
Reading symbols from /lib/x86_64-linux-gnu/libutil.so.1...Reading symbols from /usr/lib/debug//lib/x86_64-linux-gnu/libutil-2.19.so...done.
done.
Loaded symbols for /lib/x86_64-linux-gnu/libutil.so.1
Reading symbols from /lib/x86_64-linux-gnu/libexpat.so.1...(no debugging symbols found)...done.
Loaded symbols for /lib/x86_64-linux-gnu/libexpat.so.1
Reading symbols from /lib/x86_64-linux-gnu/libz.so.1...(no debugging symbols found)...done.
Loaded symbols for /lib/x86_64-linux-gnu/libz.so.1
Reading symbols from /lib/x86_64-linux-gnu/libm.so.6...Reading symbols from /usr/lib/debug//lib/x86_64-linux-gnu/libm-2.19.so...done.
done.
Loaded symbols for /lib/x86_64-linux-gnu/libm.so.6
Reading symbols from /lib64/ld-linux-x86-64.so.2...Reading symbols from /usr/lib/debug//lib/x86_64-linux-gnu/ld-2.19.so...done.
done.
Loaded symbols for /lib64/ld-linux-x86-64.so.2
0x00007f26034c28f3 in __select_nocancel () at ../sysdeps/unix/syscall-template.S:81
81	../sysdeps/unix/syscall-template.S: 没有那个文件或目录.
(gdb) py-bt
Traceback (most recent call first):
  File "/home/ryefccd/env/server18/debug/bar.py", line 6, in is_num
    time.sleep(30)
  File "start.py", line 11, in <module>
    print("tmp1 is num: %s by bar.is_num func" % bar.is_num(tmp1))
(gdb) py-locals 
x = '123'
start = 48
end = 57
flag = True
time = <module at remote 0x7f2603a5c548>
```


###  参考链接

 - [https://www.wzdftpd.net/blog/python-scripts-in-gdb.html](https://www.wzdftpd.net/blog/python-scripts-in-gdb.html)
 - [https://sourceware.org/gdb/wiki/PythonGdbTutorial](https://sourceware.org/gdb/wiki/PythonGdbTutorial)


