#!/usr/bin/env python3
"""
脚本用于生成 challenges.md 文件，其中包含所有题目的信息表格
"""

import os
import sys

# 尝试导入tomllib (Python 3.11+) 或 tomli
try:
    import tomllib  # Python 3.11+
except ImportError:
    try:
        import tomli as tomllib  # 需要安装: pip install tomli
    except ImportError:
        print("错误: 需要安装 tomli 库。请运行: pip install tomli")
        sys.exit(1)

# 定义挑战目录
CHALLENGES_CATEGORY_DIRS = ["./Web", "./Crypto", "./Misc", "./Pwn", "./Reverse"]


def read_meta_toml(challenge_path):
    """读取题目的 meta.toml 文件并提取信息"""
    meta_path = os.path.join(challenge_path, "meta.toml")

    if not os.path.exists(meta_path):
        return None

    try:
        with open(meta_path, "rb") as f:
            meta_data = tomllib.load(f)

        # 提取所需信息
        name = meta_data.get("name", "")
        author = meta_data.get("author", "")
        category = meta_data.get("category", "")
        description = meta_data.get("description", "")

        # 如果description是多行字符串，将其转换为单行
        if isinstance(description, str):
            # 将换行符替换为空格
            description = " ".join(description.splitlines())

        return {
            "name": name,
            "author": author,
            "category": category,
            "description": description,
        }
    except Exception as e:
        print(f"读取 {meta_path} 时出错: {e}")
        return None


def generate_challenges_table():
    """生成挑战信息表格"""
    challenges = []

    # 遍历所有挑战目录
    for category_dir in CHALLENGES_CATEGORY_DIRS:
        if not os.path.exists(category_dir):
            continue

        # 遍历该目录下的所有题目
        try:
            for challenge_name in os.listdir(category_dir):
                challenge_path = os.path.join(category_dir, challenge_name)

                # 检查是否为目录
                if not os.path.isdir(challenge_path):
                    continue

                # 读取题目信息
                challenge_info = read_meta_toml(challenge_path)
                if challenge_info:
                    challenges.append(challenge_info)
        except Exception as e:
            print(f"读取目录 {category_dir} 时出错: {e}")
            continue

    # 生成Markdown表格
    md_content = "# Challenges\n\n"
    md_content += "| 题目名称 | 分类 | 作者 | 描述 |\n"
    md_content += "|---------|------|------|------|\n"

    # 按分类排序
    challenges.sort(key=lambda x: (x["category"], x["name"]))

    for challenge in challenges:
        # 转义描述中的管道符
        description = challenge["description"].replace("|", "\\|")
        md_content += f"| {challenge['name']} | {challenge['category']} | {challenge['author']} | {description} |\n"

    return md_content


def main():
    """主函数"""
    md_content = generate_challenges_table()

    # 写入文件
    with open("challenges.md", "w", encoding="utf-8") as f:
        f.write(md_content)

    print("challenges.md 文件已生成！")


if __name__ == "__main__":
    main()
