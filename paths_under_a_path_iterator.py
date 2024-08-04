import os


def print_subdirectories(directory):
    # 使用 os.walk() 遍历目录树
    for root, dirs, _ in os.walk(directory):
        # 打印当前路径下的所有子目录
        for dir in dirs:
            print(os.path.join(root, dir))


# 指定要搜索的目录
directory = 'S:\Gallery\【二次元】Anime World／二次元世界／アニメの世界'

# 调用函数
print_subdirectories(directory)

if __name__ == '__main__':
    print_subdirectories('PyCharm')
