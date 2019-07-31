# -*- coding: utf-8 -*-
from pinyin import PinYin

if __name__ == '__main__':
    
    test = PinYin(no_digit=False, no_letter=False)
    
    test.load_word()
    
    s = '钓鱼岛是中国的'
    
    print('"%s" 转换成拼音: %s' % (s, test.to_pinyin(s)))
    print('"%s" 转换成带分隔符的拼音: %s' % (s, test.to_pinyin(s, join_with=' ')))
    print('"%s" 转换成带分隔符的拼音(保留多音字): %s' % (s, test.to_pinyin(s, join_with=' ', multi=True)))
    print('"%s" 转换成带分隔符的拼音且首字符大写: %s' % (s, test.to_pinyin(s, join_with=' ', capitalize=True)))
    print('"%s" 转换成带分隔符的拼音且首字符大写(保留多音字): %s' % (s, test.to_pinyin(s, join_with=' ', capitalize=True, multi=True)))
    print('"%s" 转换成首字母缩写: %s' % (s, test.to_abbr(s)))
    print('"%s" 转换成首字母缩写(保留多音字): %s' % (s, test.to_abbr(s, multi=True)))

    s = '加油中国！加油华为！你行！'
    
    print('\n\n原始字符串："%s"' % s )
    # 原始字符串："加油中国！加油华为！你行！"
    
    print('拼音首字母： %s ' % test.to_abbr(s))
    
    print('全拼: %s' % test.to_pinyin(s))
    
    print('转换成拼音（保留多音字）： %s ' % test.to_pinyin(s, capitalize=True, multi=True))
    print('转换拼音首字母缩写： %s ' % test.to_abbr(s, multi=True))
    