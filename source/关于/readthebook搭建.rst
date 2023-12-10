============================
readthebook搭建
============================

前言
==============

一个比较好的教程，是step by step的，由浅入深。但这需要掌握之后，再来写文档。
这里是边尝试，边写文档。所以写结论性的内容，比较方便。由浅入深的写，需要前后反复修改，有点麻烦。
本文将按照如下逻辑展开：在本地构建; 上传到readthebook中;

相关参考：
`readthedocs官方文档 <https://docs.readthedocs.io/en/stable/tutorial/>`_ 、
`Sphinx + Read the Docs 从懵逼到入门 <https://z.itpub.net/article/detail/A330D3FEC5B63BEB1005AD0967DAA6D3>`_

在本地构建内容
==============

先安装一些包。可能有些包，我们目前不知道它的作用，在后续使用的过程中自然可知。

建议在 `python-虚拟环境 <https://docs.python.org/zh-cn/3/library/venv.html>`_ 中安装这些包。

.. code-block:: shell

    # 准备python环境
    python3 --version
    pip --version
    pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

    # 安装sphinx
    # 没有使用sudo安装，确保~/.local/bin在PATH中
    pip install sphinx # 文档构建工具
    pip install sphinx-autobuild # 构建并创建一个server
    pip install recommonmark # 支持 Markdown 语法
    pip install sphinx_markdown_tables # 支持 markdown 的表格语法


安装完 ``sphinx`` 之后，可以使用下面的工具。

.. code-block:: shell

    sphinx-apidoc:用于自动生成Sphinx源代码。它可以为Python模块、类、方法等生成reStructuredText文档。
    sphinx-autobuild:用于构建Sphinx文档集。当在source/中检测到更改时，将重建文档并自动重新加载任何打开的浏览器窗口，而结果则输出在source/_build/html中 。
    sphinx-autogen:用于自动生成Sphinx项目所需的所有文件和目录结构。它可以为Python模块、类、方法等生成reStructuredText文档。
    sphinx-build:用于构建Sphinx文档集。它可以根据指定的配置选项构建文档集，并将其输出到指定的目录中。
    sphinx-quickstart:用于快速创建一个基本的Sphinx项目。它会自动创建一个conf.py文件和一个index.rst文件，以及一个docs目录和一个_build目录 。

使用 ``sphinx-quickstart`` 构建一个基本项目。可以在一个空仓库目录中，执行该命令。执行后生成如下内容。

.. code-block::

    # 我选择独立的源文件和构建目录-这样build和source在不同目录
    # 语言选zh_CN
    sphinx-quickstart

    │   make.bat # 构建脚本
    │   Makefile # 构建脚本
    │
    ├───build # 生成的文件的输出目录。
    └───source
        │   conf.py # 存放 Sphinx 的配置
        │   index.rst # 文档项目起始文件
        │
        ├───_static # 静态文件目录
        └───_templates # 模板目录


构建html文档,并启动http服务。

.. code-block::

    sphinx-autobuild source build/html

进一步修改
==============

修改目录
-------------
修改 ``index.rst`` 。

修改配置
--------------
具体可以参考仓库中的 ``conf.py``。
1. 修改主题为 ``sphinx_rtd_theme``。
2. 修改 edit-source-links。

添加.gitignore和requirements
----------------------------
1. ``.gitignore`` 可以复制 `the tutorial GitHub template <https://github.com/readthedocs/tutorial-template/blob/main/.gitignore>`_ 中的文件。
2. ``requirements`` 不建议用 ``pip freeze > requirements.txt`` 生成。因为当前环境和 ``conf.py`` 指定的环境可能不同。手动写下就好，见仓库。

添加评论功能
----------------------------
使用的扩展是： `sphinx-comments <https://github.com/executablebooks/sphinx-comments>`_

第一次配置有点难搞，我搞了半天才明白。注意点有两个：在需要添加评论的后面,添加javascript脚本; 脚本使用myst_parser语法。
详细可以该仓库的配置。


readthedocs导入项目
===================

将上面编辑好的内容，提交的github仓库。然后注册一个 `readthedocs <https://readthedocs.org/dashboard/>`_ ,
在里面导入仓库即可。可参考: `Read the Docs tutorial <https://docs.readthedocs.io/en/stable/tutorial/>`_。

rst使用
==============

使用markdown格式，图片不会自动拷贝到合适的位置。但是 
`Getting started with Sphinx <https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html#using-markdown-with-sphinx>`_
里面的 `MyST <https://myst-parser.readthedocs.io/en/latest/intro.html>`_
可以使用仓库的本地图片 
`Images and figures <https://myst-parser.readthedocs.io/en/latest/syntax/images_and_figures.html>`_ 。
不知道MyST是如何做到的。

快速学习下rst好了，它会拷贝图片到build目录。

rst语法参考: `reStructuredText 语法 <https://3vshej.cn/rstSyntax/index.html>`_ 。

我是在vscode中安装 ``restructuredtext`` ,编辑rst文件的。
但是插件没配置好，黑乎乎的, 没啥作用。
参考 `在Visual Studio Code中使用 <https://zzqcn.github.io/design/rest/with_vscode.html>`_。

