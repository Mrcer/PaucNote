# 咩咩的笔记

这是咩咩存放笔记的地方，供朋友们参考学习使用。因为笔记是为自己写的，内容必定存在不少不严谨和纰漏，只是觉得这种这么适合分享的Markdown笔记不放出了太浪费罢了。如果存在知识性错误或排版问题欢迎在[仓库首页](https://gitee.com/mrcer/pauc-note)`issue`或`pull request`，也欢迎在issue区提出合理建议。另外也欢迎想来参观[我的博客](https://mrcer.gitee.io/blog)哦qwq。

# 项目构建

本项目使用[MkDocs](https://www.mkdocs.org/)，依赖`MathJax`来渲染公式。完整构建过程如下：

1. 安装Python

    Windows在[官网](https://www.python.org/)下安装包安装，Linux用户的话。。不用教了吧。

2. 安装mkdocs及相关插件

    `pip install mkdocs-material`大概能解决了吧，我也不知道依赖什么，不行就看着错误装上就是了。
    
3. 构建项目运行

    命令行环境下进入项目根目录，执行`mkdocs build`构建，或者直接`mkdocs serve`预览