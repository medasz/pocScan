import os
import sys


class framework():
    def __init__(self, urls, plugin=''):
        self.urls = urls
        self.plugin = plugin
        self.result = list()

    def exploit(self):
        # 导入插件
        sys.path.append(self.plugin)
        plugins = os.listdir(self.plugin)
        for target in self.urls:
            for plugin in plugins:
                try:
                    if os.path.splitext(plugin)[1] == '.py':
                        module = __import__(os.path.splitext(plugin)[0])
                        rs = module.Exploit(target)
                        rs.verity()
                        if rs.result['status']:
                            self.result.append(
                                [target, os.path.splitext(plugin)[0], rs.result['status'], rs.result['info']])
                except Exception as e:
                    print(e)