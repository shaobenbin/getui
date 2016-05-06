## 关于项目

#### 1. 为什么有这个项目
这是个推的官方代码，[传送门](http://docs.getui.com/server/python/start/#python-sdk)

堂堂一个官方文档，没有提供pip install也就算了，也没有提供python setup.py install。难道非要让我们把源代码拷贝进去？？太low了。因此临时看了下官方文档自己写了个setup.py将就这用


#### 2. 版本号
基于个推4.0.1.0版本，只支持python 2.x

#### 3. 安装方式
python setup.py install

#### 4. 使用示例（非常重要）
由于官方的包的目录结构是：

	* .idea
	* google
	* igetui
	* payload
	* protbuf
	* 各种.py文件

这种方式我个人认为容易引起包混乱，因此我加了一个顶层目录(getui)变成了

* getui
	* .idea
	* google
	* igetui
	* payload
	* protbuf
	* 各种.py文件

因此<b>包引用都要加一个getui.xxx的方式</b>。比如官方示例[传送门](http://docs.getui.com/server/python/start/#python-sdk_1)的代码会变成

```

# -*- coding: utf-8 -*-

# 只变动了这里....
from getui.igetui.igt_message import IGtAppMessage
from getui.igetui.template.igt_link_template import LinkTemplate
from getui.igt_push import IGeTui

# 剩下的代码一致

```



