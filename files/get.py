from os import walk, path

# 使用举例
# from bllools.files import get
# dir = 'D:/workplace/CCPD/2B/ASC'
# getFiles = get.GetFile(dir, suffix={'VO.java', 'vo.java', 'Vo.java'})
# files = getFiles.all_files()

'''
此类针对文件的查找功能
基础的功能是将路径下所有文件都查询出来
再此基础上，如果传入前缀(prefix)或尾缀(suffix)，则会将符合文件名规则的文件过滤获取
'''
class GetFile():

    def __init__(self, dirc, suffix=[], prefix=[]):
        self.prefix = prefix
        self.suffix = suffix
        self.dirc = dirc
        # 判断是否需要以文件尾缀进行过滤
        self.need_suffix = False if self.suffix is None or len(self.suffix) == 0 else True
        # 判断是否需要以文件前缀进行过滤
        self.need_prefix = False if self.prefix is None or len(self.prefix) == 0 else True

    '''
    该方法为递归方法
    在初始化时已经设置了根目录， 所以在使用该方法时不要传入路径(new_dir)这个参数
    最后会将符合条件的文件以绝路路径列表的形式返回
    '''
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

