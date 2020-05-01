# TPandas Platform

## 测试平台后端项目

[TOC]

#### 核心组件说明：

1. loguru [日志框架]

```python
# 在模块文件中，如果需要输出日志，直接导入logger即可，代码如下所示： 
from loguru inport logger
logger.debug('这是一条debug日志')
logger.info('这是一条info日志')
logger.warning('这是一条warning日志')
logger.error('这是一条error日志')

# 如果想捕获整个函数的异常日志并输出，可使用@logger.catch装饰器，代码如下所示：
@logger.catch
def test_function():
    a = '1'
    b = 3
    c = a + b
    print(c)

test_function()
```
捕获的错误日志如下：
![image-20200501171726184](C:\Users\wf193\AppData\Roaming\Typora\typora-user-images\image-20200501171726184.png)



### 1. accounts-用户管理

### 2. managements-测试管理

### 3. runners-测试执行

