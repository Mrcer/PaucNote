# 咩咩的共享笔记仓库

这是咩咩和朋友们存放笔记的地方，并通过Gitee Pages展示在[这里](https://mrcer.gitee.io/pauc-note)，供大家参考学习使用。因为笔记是个人写的，内容必定存在一定不严谨和纰漏，请参考笔记的同学保持质疑精神，最好参考着教材看。如果存在知识性错误或排版问题欢迎在[仓库首页](https://gitee.com/mrcer/pauc-note)`issue`或`pull request`，也欢迎在issue区提出合理建议。另外也欢迎想来参观[我的博客](https://mrcer.gitee.io/blog)哦qwq。

# 项目构建

本项目使用[MkDocs](https://www.mkdocs.org/)，依赖`MathJax`来渲染公式。完整构建过程如下：

1. 安装Python

    Windows在[官网](https://www.python.org/)下安装包安装，Linux用户的话。。不用教了吧。

2. 安装mkdocs及相关插件

    `pip install mkdocs-material`大概能解决了吧，我也不知道依赖什么，不行就看着错误装上就是了。
    
3. 构建项目运行

    命令行环境下进入项目根目录，执行`mkdocs build`构建，或者直接`mkdocs serve`预览。预览有自动同步功能，不需要频繁重启

# 参与共享

欢迎参与笔记共享！

## 远程开发准备

你可以以访客身份通过`fork`开发，然后提`pull request`（我没试过，应该是吧）。如果是认识我的朋友，可以微信私我获得开发者权限。

在拥有远程仓库开发权后，将仓库克隆下来，然后参考上面准备好`mkdocs`环境，即可完成准备工作。更多细节请自学git，或者私信问我

## 整理笔记

笔记以markdown形式保存在`docs`文件夹，并分类存放。在添加完笔记后请在`mkdocs.yml`中注册，里面已经说明了注册方式。注册完后记得预览，查看无误后再提交。

一些markdown上的提醒：

1. 引用的渲染方式相对其他软件有比较大不同，请确定这是你想要的效果
   > 这是引用
2. mkdocs对格式要求更严格，比如这里的序号前后需要换行，不然会挤在一起。序号的判定也挺迷的，搞不懂就像我一样用黑点吧(x-x)
3. display style的latex（也就是双美元公式）要单独拎出来，前后换行，美元符号单独一行

不要问我为什么这么多限制，这是mkdocs的事，我也不懂。懂的同学欢迎issue

如果喜欢的话它也有独特而好看的东西，你可以在page里查看：

对于图片，你可以放在图床上，也可以像我一样放在每个课程笔记目录下的`image`文件夹里，然后用相对路径引用。注意文件不要太大，gitee page可能带不动。

## 上传笔记

一切准备就绪后，**请记得构建项目**，然后再`add`、`commit`、`push`。完成后要手动在“服务”->“Gitee Pages”里更新页面。如果没有权限，私我。