import os

# 定义图片文件夹和目标文件夹的路径
image_folder = '/data0/fqy/DOTA_SS/origin/images/'  # 修改为你的图片文件夹路径
target_folder = '/data0/fqy/DOTA_SS/origin/labelTxt/'  # 修改为你的目标文件夹路径

# 遍历图片文件夹中的图片文件
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        # 生成对应名称的txt文件路径
        txt_filename = os.path.splitext(filename)[0] + '.txt'
        txt_filepath = os.path.join(target_folder, txt_filename)
        
        # 创建空的txt文件
        with open(txt_filepath, 'w') as txt_file:
            pass  # 创建一个空文件

print('文本文件创建完成')
