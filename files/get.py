from os import walk, path


class GetFile():

    def __init__(self, dirc, suffix=[], prefix=[]):
        self.prefix = prefix
        self.suffix = suffix
        self.dirc = dirc
        # 判断是否需要以文件尾缀进行过滤
        self.need_suffix = False if self.suffix is None or len(self.suffix) == 0 else True
        # 判断是否需要以文件前缀进行过滤
        self.need_prefix = False if self.prefix is None or len(self.prefix) == 0 else True

    def __str__(self):
        print("获取路径 ", self.dirc, " 下所有文件")

    def all_files(self, new_dir:str = ""):
        result_files = [];

        for home, dirs, files in walk(self.dirc if new_dir is None or new_dir == "" else new_dir):
            for currdir in dirs:
                result_files += self.all_files(path.join(home, currdir))
            for file in files:
                if self.need_suffix == False and self.need_prefix == False:
                    result_files += [path.join(home, file)]
                else:
                    suffix = prefix = False
                    if self.need_suffix:
                        for cursuf in self.suffix:
                            if file.endswith(cursuf):
                                suffix = True
                                break
                    else:
                        suffix = True
                    if self.need_prefix:
                        for curpre in self.prefix:
                            if file.startswith(curpre):
                                prefix = True
                                break
                    else:
                        prefix = True
                    if suffix and prefix:
                        result_files += [path.join(home, file)]
        return result_files

