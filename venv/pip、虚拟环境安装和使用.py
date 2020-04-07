"""
pip 命令
"""
pip -v 查看pip版本
pip install numpy == 2.1
pip freeze > requirement.txt
pip install -r requirement.txt
pip install xxxx.whl
pip install -U pip 升级
pip --help 获取帮助
pip --version 显示版本和路径
pip install SomePackage              # 最新版本
pip install SomePackage==1.0.4       # 指定版本
pip install 'SomePackage>=1.0.4'     # 最小版本
pip install --upgrade SomePackage 升级包
pip search SomePackage 搜索包
pip list 列出已安装的包
pip list -o 查看可升级的包

"""
虚拟环境
"""