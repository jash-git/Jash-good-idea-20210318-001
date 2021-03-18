#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

Mat src;
int alpha = 20, beta = 40;
Rect rect;

void illuminationChange_Callback(int, void*)
{
  Mat dst;
  Mat mask = Mat::zeros(src.size(), src.type());
  rectangle(mask, rect, Scalar::all(255), -1);
  illuminationChange(src, mask, dst, alpha / 100.0, beta / 100.0);
  imshow("illuminationChange", dst);
}

int main()
{
  src = imread("1.png");
  rect = selectROI(src, true, false);

  namedWindow("illuminationChange", WINDOW_NORMAL);
  createTrackbar("alpha", "illuminationChange", &alpha, 300, illuminationChange_Callback);
  createTrackbar("beta", "illuminationChange", &beta, 300, illuminationChange_Callback);
  illuminationChange_Callback(0, 0);

  waitKey();
  return 0;
}