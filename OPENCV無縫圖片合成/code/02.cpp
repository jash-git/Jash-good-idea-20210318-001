#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

Mat src;
int r = 100, g = 100, b = 100;
Rect rect;

void colorChange_Callback(int, void *)
{
  Mat dst;
  Mat mask = Mat::zeros(src.size(), src.type());
  rectangle(mask, rect, Scalar::all(255), -1);
  colorChange(src, mask, dst, r/100.0, g/100.0, b/100.0);
  imshow("colorChange", dst);
}

int main()
{
  src = imread("4.jpg");
  rect = selectROI(src, true, false);
  namedWindow("colorChange", WINDOW_NORMAL);
  createTrackbar("R", "colorChange", &r, 250, colorChange_Callback);
  createTrackbar("G", "colorChange", &g, 250, colorChange_Callback);
  createTrackbar("B", "colorChange", &b, 250, colorChange_Callback);
  colorChange_Callback(0, 0);

  waitKey();
  return 0;
}