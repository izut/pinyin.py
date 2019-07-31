# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

__version__ = '0.9'
__all__ = ["PinYin"]

import os.path


class PinYin(object):
    """
    中文转拼音
    """
    no_digit: bool
    no_letter: bool

    def __init__(self, dict_file='word.data', no_digit: bool = True, no_letter: bool = True):
        """
        :param dict_file: defult file name
        :param no_digit: (optional) no numbers[0-9], default: True
        :param no_letter: (optional) no letters[a-zA-Z], default: True
        """
        
        self.word_dict = {}
        self.dict_file = 'word.data'
        self.no_digit = no_digit
        self.no_letter = no_letter

    def load_word(self):
        """
        加载字典文件，字典文件已修改分隔符为逗号，节省75KB
        :return:
        """
        if not os.path.exists(self.dict_file):
            raise IOError("NotFoundFile")

        with open(self.dict_file, 'r') as f_obj:
            for f_line in f_obj.readlines():
                line = f_line.split(':')
                self.word_dict[line[0]] = line[1]

    def hanzi2pinyin(self, string: str, split: str=None):
        """
        修改为python3, 与hanzi2piinyin_split合并
        :param string:
        :param split:
        :return:
        """
        result = []
        string = str(string)
        for char in string:
            key = '%X' % ord(char)
            result.append(self.word_dict.get(key, char).split()[0][:-1].lower())
        
        if isinstance(split, str):
            return split.join(result)
        else:
            return result
        
    def hanzi2pinyin_split(self, string, split=""):
        """
        用分隔符连接的拼音
        :param string: 中文
        :param split: 分隔符
        :return:
        """
        # return split.join(self.hanzi2pinyin(string))
        return self.hanzi2pinyin(string, split=split)
    
    def to_pinyin(self, string, capitalize: bool=False, multi: bool=False, join_with: str=None):
        """
        转换成拼音
        :param string: 中文字符串
        :param capitalize: 是否首字母大写
        :param multi: 是否有多单字是生成多个结果
        :param join_with: 是否拼接单字拼音，None:不拼接，str:拼接
        :return:
        """
        multi_result = [[]]
        result = []
        string = str(string)
        cap = lambda s: s.capitalize() if capitalize else s.lower()
        
        for char in string:
            
            key = '%X' % ord(char)
            pinyin_list = self.word_dict.get(key, None)
            
            _pinyin = ''        # 并不是每个字符都能转换为拼音，默认为空
            
            # 字库中无该字
            if pinyin_list is None:
                if char.isalpha() and not self.no_letter:
                    # 保留字母
                    _pinyin = char
                elif char.isdigit() and not self.no_digit:
                    # 保留数字
                    _pinyin = char
                
                if not _pinyin:
                    continue
                    
                if multi:
                    multi_result = [r.append(_pinyin) for r in multi_result]
                else:
                    result.append(_pinyin)
                    
            else:
                _pinyins = list(set([r[:-1] for r in pinyin_list.split()]))
                if not multi:
                    result.append(cap(_pinyins[0]))
                    continue
                    
                if len(_pinyins) == 1:
                    _pinyin = cap(_pinyins[0])
                    multi_result = [m + [_pinyin] for m in multi_result]
                else:
                    # print('"%s" 读音：%s' % (char, _pinyins))
                    old = multi_result[:]
                    multi_result = []
                    for _pinyin in _pinyins:
                        _pinyin = cap(_pinyin)
                        multi_result.extend([m + [_pinyin] for m in old])
                    

        if multi:
            if isinstance(join_with, str):
                return [join_with.join(ret) for ret in multi_result]
            else:
                return multi_result
        else:
            if isinstance(join_with, str):
                return join_with.join(result)
            else:
                return result
        
    
    def to_abbr(self, string, multi: bool=False):
        """
        中文拼音首字母缩写
        :param string: 中文字符串
        :param multi: 是保留多单字
        :return: 当multi=True, 返回list, 否则返回str
        """
        result = self.to_pinyin(string=string, capitalize=True, multi=multi)
        
        if multi:
            return list(set([''.join([c[0] for c in py]) for py in result]))
            # return result
        else:
            return ''.join([c[0] for c in result])
        
    
    
# edit by izut@163.com
# if __name__ == "__main__":
#     test = PinYin()
#     test.load_word()
#     string = "钓鱼岛是中国的"
#     print "in: %s" % string
#     print "out: %s" % str(test.hanzi2pinyin(string=string))
#     print "out: %s" % test.hanzi2pinyin_split(string=string, split="-")
