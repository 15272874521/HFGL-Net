import os

# 定义原始文件夹路径和目标文件夹路径
source_folder = '/data0/fqy/yolov5/yolov5_obb-master/runs/val/dotav15_test_split19/obb_predictions_Txt_Merged/'  # 修改为你的原始文件夹路径
target_folder = '/data0/fqy/yolov5/yolov5_obb-master/runs/val/dotav15_test_split19/yolov5l/'  # 修改为你的目标文件夹路径

# 定义文件名映射字典
name_mapping = {
    'plane': 'small-vehicle',
    'baseball-diamond': 'large-vehicle',
    'bridge': 'plane',
    'ground-track-field': 'storage-tank',
    'small-vehicle': 'ship',
    'large-vehicle': 'harbor',
    'ship': 'ground-track-field',
    'tennis-court': 'soccer-ball-field',
    'basketball-court': 'tennis-court',
    'storage-tank': 'swimming-pool',
    'soccer-ball-field': 'baseball-diamond',
    'roundabout': 'roundabout',
    'harbor': 'basketball-court',
    'swimming-pool': 'bridge',
    'helicopter': 'helicopter'
}

# 创建目标文件夹（如果不存在）
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

# 遍历原始文件夹中的txt文件
for filename in os.listdir(source_folder):
    if filename.endswith('.txt'):
        # 提取文件名中的类别名称
        parts = filename.split('_')
        if len(parts) == 2:
            old_name = parts[1].split('.')[0]
            # 查找映射并替换为新的名称
            new_name = name_mapping.get(old_name, old_name)
            # 构建新的文件名
            new_filename = f'Task1_{new_name}.txt'
            # 构建文件的完整路径
            old_filepath = os.path.join(source_folder, filename)
            new_filepath = os.path.join(target_folder, new_filename)
            # 复制文件到目标文件夹并重命名
            os.rename(old_filepath, new_filepath)

print('文件名替换完成并保存到目标文件夹')
