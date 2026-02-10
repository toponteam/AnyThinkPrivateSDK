#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
脚本功能：
将当前目录中所有 podspec 文件，在上层目录创建对应的文件结构目录，并将自身复制在里面。
例如：AnyThinkMediationGromoreAdapter-Only.podspec
最终路径：AnyThinkPrivateSDK/AnyThinkMediationGromoreAdapter-Only/7.4.0.0.0/AnyThinkMediationGromoreAdapter-Only.podspec
"""

import os
import re
import shutil
from pathlib import Path


def get_version_from_podspec(podspec_path):
    """
    从 podspec 文件中提取 s.version 的值
    
    Args:
        podspec_path: podspec 文件路径
        
    Returns:
        版本号字符串，如果未找到则返回 None
    """
    try:
        with open(podspec_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 匹配 s.version = '版本号' 或 s.version = "版本号"
        # 支持多种格式: s.version = 'x.x.x' 或 s.version= 'x.x.x' 或带空格的情况
        patterns = [
            r's\.version\s*=\s*[\'"]([^\'"]+)[\'"]',  # 标准格式
            r'spec\.version\s*=\s*[\'"]([^\'"]+)[\'"]',  # 使用 spec 的格式
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                return match.group(1)
        
        print(f"警告: 无法从 {podspec_path} 中提取版本号")
        return None
        
    except Exception as e:
        print(f"错误: 读取文件 {podspec_path} 失败: {e}")
        return None


def create_directory_structure_and_copy(podspec_file, current_dir, parent_dir):
    """
    为 podspec 文件创建目录结构并复制文件
    
    Args:
        podspec_file: podspec 文件名
        current_dir: 当前目录路径
        parent_dir: 上层目录路径
    """
    podspec_path = os.path.join(current_dir, podspec_file)
    
    # 获取版本号
    version = get_version_from_podspec(podspec_path)
    if not version:
        print(f"跳过文件: {podspec_file} (无法获取版本号)")
        return False
    
    # 获取 podspec 文件名（不含扩展名）
    podspec_name = os.path.splitext(podspec_file)[0]
    
    # 构建目标目录路径: parent_dir/podspec_name/version/
    target_dir = os.path.join(parent_dir, podspec_name, version)
    
    # 创建目录结构
    try:
        os.makedirs(target_dir, exist_ok=True)
        print(f"创建目录: {target_dir}")
    except Exception as e:
        print(f"错误: 创建目录 {target_dir} 失败: {e}")
        return False
    
    # 复制 podspec 文件到目标目录
    target_file = os.path.join(target_dir, podspec_file)
    try:
        shutil.copy2(podspec_path, target_file)
        print(f"复制文件: {podspec_file} -> {target_file}")
        return True
    except Exception as e:
        print(f"错误: 复制文件 {podspec_file} 失败: {e}")
        return False


def main():
    """
    主函数
    """
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"当前目录: {current_dir}")
    
    # 获取上层目录
    parent_dir = os.path.dirname(current_dir)
    print(f"上层目录: {parent_dir}")
    print("-" * 60)
    
    # 查找当前目录下所有 .podspec 文件
    podspec_files = [f for f in os.listdir(current_dir) if f.endswith('.podspec')]
    
    if not podspec_files:
        print("当前目录中没有找到 .podspec 文件")
        return
    
    print(f"找到 {len(podspec_files)} 个 podspec 文件")
    print("-" * 60)
    
    # 处理每个 podspec 文件
    success_count = 0
    for podspec_file in podspec_files:
        print(f"\n处理文件: {podspec_file}")
        if create_directory_structure_and_copy(podspec_file, current_dir, parent_dir):
            success_count += 1
        print("-" * 60)
    
    # 输出统计信息
    print(f"\n完成! 成功处理 {success_count}/{len(podspec_files)} 个文件")


if __name__ == "__main__":
    main()
