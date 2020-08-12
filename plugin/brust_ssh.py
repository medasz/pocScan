class Exploit():
    def __init__(self, target):
        self.target = target
        self.result = {
            'name': 'ssh弱口令',
            'author': 'medasz',
            'type': 'ssh',
            'status': False,
            'info': '',
            'target': target
        }

    def verity(self):
        print('调用成功!')
        self.result['status'] = True
        self.result['info'] = 'xxxxx'
