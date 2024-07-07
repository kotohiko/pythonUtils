import os


def list_files(start_path):
    files_counts = 0
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        # 在py中，缩进真乃善用之物
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            files_counts = files_counts + 1
    print("The Total number of files: {}".format(files_counts))


startpath = 'S:\Gallery\【二次元】Anime World／二次元世界／アニメの世界'
list_files(startpath)

if __name__ == '__main__':
    list_files('PyCharm')
