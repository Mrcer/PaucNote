import os

ignore = [
    'javascripts',
    'index.md'
]

def print_note_dir(path):
    for filename in os.listdir(path):
        if filename.endswith(".md"):
            filename = filename[:-3]
            print(6*' ' + "- '" + filename + "': " + f"'{path.split('/')[-1]}/{filename}.md'")

def sort_by_mtime(notedir_name):
    notedir_stat = list(map(lambda x: os.stat(f'{rootdir_path}/{x}'), notedir_name))
    combination = list(zip(notedir_name, notedir_stat))
    combination.sort(key=lambda x: -x[1].st_mtime)
    notedir_name, _ = zip(*combination)
    return notedir_name

if __name__ == '__main__':
    rootdir_path = './docs'
    notedir_name = os.listdir(rootdir_path)
    notedir_name = sort_by_mtime(notedir_name)

    for notedir in notedir_name:
        if notedir in ignore:
            continue
        path = f'{rootdir_path}/{notedir}'
        print(f'以下是笔记仓库 {notedir} 对应的配置文件：')
        print_note_dir(path)
        input('回车打印下个笔记仓库的配置')