//鼠标事件绘制矩形代码看B站视频，地址：
//https://www.bilibili.com/video/BV1sa4y1s7FR?p=10
Mat src = imread("light.jpg");
Mat dst = imread("2.jpg");

Mat mask = Mat::zeros(src.rows, src.cols, src.depth());
rectangle() //绘制mask自己添加
Point center(400,200);
Mat output;
seamlessClone(src, dst, mask, center, output, NORMAL_CLONE);