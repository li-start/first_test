开发环境
=======
 - 开发工具：pycharm
 - 编程语言：python3
 - 单元测试：
 
 运行
======
  在main.py文件中，按照以下方式运行
  > #python main.py [原文文件][抄袭的文件][答案文件],如下例：
  
  > python  main.py orig.txt orig_0.8_add.txt ans.txt
 
开发者日志
======
 第一阶段
 ---------------
 
  (time:2020.9.7)

 起初看到这个题目的时候感觉无从下手，和之前学过的知识跨度太大，但是好在互联网功能强大还有身边大佬的提点，基本有了学习的方向，打算花两天时间速成 一下python基础（后来发现两天可能有点奢侈，如果只学基础并且有java和c/c++基础，python入门还算容易）

（time:2020.9.9)
- 学完python，看了一些博客和github上的代码，有了一些基本的思路：首先要做的是搭建好算法框架，把各个模块的功能区分出来，以便于把精力集中在算法上。
- 通过命令行参数读写文件。python中读写文件可以使用open，write，但是要注意所读写文件的encoding。通过命令行参数读写文件类似于c语言中的scanf，相当于java中arg[0]、arge[1]。 &nbsp;这部分如果一开始就做的话，后期每运行一次都要输入一次文件的绝对地址会很麻烦，所以这步先保留着）
- python有很多库可以用于中文分词，找了很多资料后，决定用jieba来做
- 算法部分，打算采用向量空间模型+余弦相似度的思想。复杂度取决于具体文本的长度。
- 单元测试目前还没有想法

（time:2020.9.10）

基本框架已建立。截下来就是编写代码实现各个模块的功能。最重要的当然还是算法，这两天翻了大量的博客，看了很多用来求文本相似度的算法，想过要放弃gensim，但是有些算法虽然性能方面更优秀，但理解起来真的烧脑。。。
（忘记当天上传了^_^，基本框架在main.py中可以查看）

第二阶段
-------
（time：2020.9.12)

 实现了用向量空间模型求文本相似度，但是求出来的文本相似度如下，基本都在99%以上，决定明天换一种算法
 经过这几天的学习，我发现这些求文本相似度的算法有以下几个共同点：
 - 分词并且去除停词
 - 建立算法模型
 - 建立字典，为分出来的词赋予一个值
 - 建立语料库，形成空间向量
 - 计算相似度
 我现在主要的问题集中在如何建立字典和形成词袋(语料库),所以接下去要做的就是集中精力找这方面的算法
 同时，在相似度的计算中，网上很多博客推荐的是余弦算法，但实际操作后发现这个算法存在的不足有很多比如相似结果太大没有可区分度，接下去可能会尝试一下lsi算法
 
 （time：2020.9.14）
 
 对算法进行了改进，查重率降低了
 
 第三阶段
 -----------
 
 - 单元测试
   >执行单元测试：unittest_main.py
 - 分析算法性能
 - 改进算法
 
 
 
 
 
  
