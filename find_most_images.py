#!/usr/bin/env python3
import os
import re
import frontmatter

def find_most_images_case():
    max_images = 0
    max_case_path = None
    max_case_data = None
    
    # 遍历所有州目录
    for state in os.listdir('content'):
        state_path = os.path.join('content', state)
        if not os.path.isdir(state_path):
            continue
        
        # 遍历州下的所有目录和文件
        for root, dirs, files in os.walk(state_path):
            for file in files:
                if file.endswith('.md'):
                    file_path = os.path.join(root, file)
                    try:
                        # 读取markdown文件的front matter
                        post = frontmatter.load(file_path)
                        if 'images' in post.metadata:
                            images = post.metadata['images']
                            if isinstance(images, list):
                                image_count = len(images)
                                if image_count > max_images:
                                    max_images = image_count
                                    max_case_path = file_path
                                    max_case_data = post
                    except Exception as e:
                        pass
    
    return max_case_path, max_case_data, max_images

if __name__ == '__main__':
    case_path, case_data, image_count = find_most_images_case()
    if case_path:
        print(f"案件路径: {case_path}")
        print(f"图片数量: {image_count}")
        print(f"案件标题: {case_data.get('title', '未命名')}")
        print(f"图片列表: {case_data.get('images', [])}")
    else:
        print("未找到包含图片的案件")