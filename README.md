# python-opencv-face-tk-aardio
界面是使用的aardio绘制在aardio上绘制界面后通过使用GUI2Python库将界面到出成tk的ui代码
优势就是结合两者都优势，即一个有图形化界面但是python安装库之后本身也需要安装对应库环境，
一个python原生界面但是没有图像化界面难以使用，使用opencv获取本地图片获取一帧后在tk的label控件上进行显示
之后重复调用摄像头不断更新获取到的图片将其保存然后通过tk处理后通过tk的label更新函数更新到label控件上
这样就出现在tk的ui上显示摄像头视频的现象，之后之后再通过opencv的级联分类器进行人脸识别框选即可
