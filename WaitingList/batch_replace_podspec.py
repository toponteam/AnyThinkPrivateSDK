#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量替换 .podspec 文件中的占位符脚本
使用方法：修改下面的配置项，然后运行 python3 batch_replace_podspec.py
"""

import os
import re
import glob


# ==================== 配置区域 ====================

# 1. 要发的adapter版本名称，注意有些是5位，有些是4位，如Gromore是7.4.0.0.0
VERSION_PLACEHOLDER_REPLACEMENT = "7.4.0.0.0"

# 2. adapter前缀，AnyThink 或 TPN
#    注意：如果配置为 TPN，还会将文件名中的 AnyThink 修改为 TPN
PREFIX_PLACEHOLDER_REPLACEMENT = "AnyThink"

# 3. 个性化占位符，默认直接移除（设置为空字符串）
#    如果需要替换为其他字符串，请修改此配置
PERSONALIZE_PLACEHOLDER_REPLACEMENT = ""

# 4. #{s.version} 替换为当前 OSS 上的 adapter 版本号
#    例如：7.4.0.0.0 注意有些是5位，有些是4位，如Gromore是7.4.0.0.0
VERSION_VARIABLE_REPLACEMENT = "7.4.0.0.0"

# 5. core版本占位符，默认 6.4.94
CORE_VERSION_PLACEHOLDER_REPLACEMENT = "6.4.94"

# 6. homepage 配置，替换 s.homepage 的值
HOMEPAGE_REPLACEMENT = "https://github.com/toponteam/AnyThinkPrivateSDK"

# ==================== 配置结束 ====================


def replace_in_file(file_path, replacements, homepage_url=None):
    """
    在文件中执行字符串替换
    
    Args:
        file_path: 文件路径
        replacements: 替换规则字典 {旧字符串: 新字符串}
        homepage_url: homepage URL，如果提供则替换 s.homepage 的值
    
    Returns:
        是否进行了替换
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 执行所有替换
        for old_str, new_str in replacements.items():
            content = content.replace(old_str, new_str)
        
        # 如果配置了 homepage，使用正则替换 s.homepage 的值
        if homepage_url:
            # 匹配 s.homepage = '...' 或 s.homepage = "..."
            homepage_pattern = r"(s\.homepage\s*=\s*['\"])([^'\"]*?)(['\"])"
            content = re.sub(homepage_pattern, rf'\1{homepage_url}\3', content)
        
        # 如果内容有变化，写回文件
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    
    except Exception as e:
        print(f"❌ 处理文件 {file_path} 时出错: {e}")
        return False


def rename_file_if_needed(file_path, prefix):
    """
    如果配置了 TPN 前缀，将文件名中的 AnyThink 替换为 TPN
    
    Args:
        file_path: 原文件路径
        prefix: 配置的前缀
    
    Returns:
        新文件路径（如果重命名了）或原文件路径
    """
    if prefix == "TPN" and "AnyThink" in os.path.basename(file_path):
        dir_name = os.path.dirname(file_path)
        old_filename = os.path.basename(file_path)
        new_filename = old_filename.replace("AnyThink", "TPN")
        new_file_path = os.path.join(dir_name, new_filename)
        
        try:
            os.rename(file_path, new_file_path)
            print(f"📝 重命名文件: {old_filename} -> {new_filename}")
            return new_file_path
        except Exception as e:
            print(f"❌ 重命名文件失败 {file_path}: {e}")
            return file_path
    
    return file_path


def main():
    """主函数"""
    print("=" * 60)
    print("🚀 批量替换 Podspec 文件工具")
    print("=" * 60)
    print("\n📋 当前配置:")
    print(f"  版本名称: (version_placeholder) -> {VERSION_PLACEHOLDER_REPLACEMENT}")
    print(f"  前缀: (prefix_placeholder) -> {PREFIX_PLACEHOLDER_REPLACEMENT}")
    print(f"  个性化标识: (personalize_placeholder) -> '{PERSONALIZE_PLACEHOLDER_REPLACEMENT}'")
    print(f"  版本变量: #{{s.version}} -> {VERSION_VARIABLE_REPLACEMENT}")
    print(f"  Core版本: (core_version_placeholder) -> {CORE_VERSION_PLACEHOLDER_REPLACEMENT}")
    print(f"  Homepage: s.homepage -> {HOMEPAGE_REPLACEMENT}")
    print()
    
    # 获取当前目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📁 工作目录: {current_dir}\n")
    
    # 查找所有 .podspec 文件
    podspec_files = glob.glob(os.path.join(current_dir, "*.podspec"))
    
    if not podspec_files:
        print("❌ 未找到任何 .podspec 文件")
        return
    
    print(f"✅ 找到 {len(podspec_files)} 个 .podspec 文件\n")
    
    # 构建替换规则
    replacements = {
        "(version_placeholder)": VERSION_PLACEHOLDER_REPLACEMENT,
        "(prefix_placeholder)": PREFIX_PLACEHOLDER_REPLACEMENT,
        "(personalize_placeholder)": PERSONALIZE_PLACEHOLDER_REPLACEMENT,
        "#{s.version}": VERSION_VARIABLE_REPLACEMENT,
        "(core_version_placeholder)": CORE_VERSION_PLACEHOLDER_REPLACEMENT,
    }
    
    # 处理每个文件
    success_count = 0
    renamed_count = 0
    
    for file_path in podspec_files:
        filename = os.path.basename(file_path)
        print(f"🔄 处理文件: {filename}")
        
        # 执行替换
        if replace_in_file(file_path, replacements, HOMEPAGE_REPLACEMENT):
            print(f"  ✅ 替换完成")
            success_count += 1
        else:
            print(f"  ℹ️  无需替换（文件中没有找到占位符）")
        
        # 如果需要，重命名文件
        new_file_path = rename_file_if_needed(file_path, PREFIX_PLACEHOLDER_REPLACEMENT)
        if new_file_path != file_path:
            renamed_count += 1
        
        print()
    
    # 输出总结
    print("=" * 60)
    print("✨ 处理完成!")
    print(f"  总文件数: {len(podspec_files)}")
    print(f"  成功替换: {success_count}")
    print(f"  重命名文件: {renamed_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
