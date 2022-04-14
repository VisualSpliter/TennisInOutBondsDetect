import cv2

video_path = 'C:/Users/Compu/Documents/GitHub/TennisInOutBondsDetect/vidtoimg/vid/VID_20220414_152954.mp4'  # 视频地址
output_path = 'C:/Users/Compu/Documents/GitHub/TennisInOutBondsDetect/vidtoimg/img/VID_20220414_152954'  # 输出文件夹
interval = 5  # 每间隔10帧取一张图片

if __name__ == '__main__':
    num = 1
    vid = cv2.VideoCapture(video_path)
    while vid.isOpened():
        is_read, frame = vid.read()
        if is_read:
            if num % interval == 1:
                file_name = 'VID_20220414_152954'+'%08d' % num
                cv2.imwrite(output_path + str(file_name) + '.jpg', frame)
                # 00000111.jpg 代表第111帧
                cv2.waitKey(1)
            num += 1

        else:
            break
