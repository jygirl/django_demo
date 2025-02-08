## [**配置环境**](https://joe-2002.github.io/sweettalk-django4.2/#/contents/P01?id=%e9%85%8d%e7%bd%ae%e7%8e%af%e5%a2%83)

### [**创建虚拟环境**](https://joe-2002.github.io/sweettalk-django4.2/#/contents/P01?id=%e5%88%9b%e5%bb%ba%e8%99%9a%e6%8b%9f%e7%8e%af%e5%a2%83)

`python -m venv erp_venv`

`erp_venv`  为虚拟环境的名字

创建 Python 虚拟环境，并将其安装在你当前所在目录下的 `erp_venv` 文件夹中。虚拟环境可以帮助你隔离不同的项目的依赖库，这样可以避免项目间的库版本冲突。

### [**启动虚拟环境**](https://joe-2002.github.io/sweettalk-django4.2/#/contents/P01?id=%e5%90%af%e5%8a%a8%e8%99%9a%e6%8b%9f%e7%8e%af%e5%a2%83)

进入虚拟环境目录

`cd erp_venv`

在目录下执行命令，启动虚拟环境

`./Scripts/activate` （Unix/Linux风格）：

- 正斜杠 "/" 用作路径分隔符。
- 在Unix/Linux和类Unix系统中，正斜杠是用于表示文件路径的常见方式。
- 通常用于在Unix/Linux系统上激活虚拟环境，比如Python虚拟环境。

`.\Scripts\activate`（Windows风格）：

- 反斜杠 "\" 用作路径分隔符。
- 在Windows操作系统中，反斜杠是用于表示文件路径的常见方式。
- 通常用于在Windows系统上激活虚拟环境，比如Python虚拟环境。

`cd` <你的虚拟环境目录名称>

`.\Scripts\activate` 激活虚拟环境

<aside>
💡

[无法加载文件\env\Scripts\Activate.ps1，因为在此系统上禁止运行脚本_运行ps脚本提示禁止运行-CSDN博客](https://www.notion.so/env-Scripts-Activate-ps1-_-ps-CSDN-0b96c7a914bc455aa2553b9f9cba6fc5?pvs=21) 

</aside>

### [**退出虚拟环境**](https://joe-2002.github.io/sweettalk-django4.2/#/contents/P01?id=%e9%80%80%e5%87%ba%e8%99%9a%e6%8b%9f%e7%8e%af%e5%a2%83)

在目录下执行命令，退出虚拟环境

`deactivate`