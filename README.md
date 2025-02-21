pinyin.py
=========

汉字转拼音,With Python
在原来的基础上增加多单字，首字母大写，保留字母、数字，首字母缩写等功能。

Example:

    from pinyin import PinYin
    
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
    
    s = '加油中国！加油HW!想要P30!'
    print('"%s" 转换成拼音: %s' % (s, test.to_pinyin(s, join_with=' ', capitalize=True)))
    print('"%s" 转换成缩写: %s' % (s, test.to_abbr(s)))
    


Out:

    "钓鱼岛是中国的" 转换成拼音: ['diao', 'yu', 'dao', 'shi', 'zhong', 'guo', 'di']
    "钓鱼岛是中国的" 转换成带分隔符的拼音: diao yu dao shi zhong guo di
    "钓鱼岛是中国的" 转换成带分隔符的拼音(保留多音字): ['diao yu dao shi zhong guo di', 'diao yu dao shi zhong guo de']
    "钓鱼岛是中国的" 转换成带分隔符的拼音且首字符大写: Diao Yu Dao Shi Zhong Guo Di
    "钓鱼岛是中国的" 转换成带分隔符的拼音且首字符大写(保留多音字): ['Diao Yu Dao Shi Zhong Guo Di', 'Diao Yu Dao Shi Zhong Guo De']
    "钓鱼岛是中国的" 转换成首字母缩写: DYDSZGD
    "钓鱼岛是中国的" 转换成首字母缩写(保留多音字): ['DYDSZGD']


    原始字符串："加油中国！加油华为！你行！"
    拼音首字母： JYZGJYHWNH 
    全拼: ['jia', 'you', 'zhong', 'guo', 'jia', 'you', 'hua', 'wei', 'ni', 'heng']
    转换成拼音（保留多音字）： [['Jia', 'You', 'Zhong', 'Guo', 'Jia', 'You', 'Hua', 'Wei', 'Ni', 'Heng'], ['Jia', 'You', 'Zhong', 'Guo', 'Jia', 'You', 'Hua', 'Wei', 'Ni', 'Hang'], ['Jia', 'You', 'Zhong', 'Guo', 'Jia', 'You', 'Hua', 'Wei', 'Ni', 'Xing']] 
    转换拼音首字母缩写： ['JYZGJYHWNH', 'JYZGJYHWNX'] 
    "加油中国！加油HW!想要P30!" 转换成拼音: Jia You Zhong Guo Jia You H W Xiang Yao P 3 0
    "加油中国！加油HW!想要P30!" 转换成缩写: JYZGJYHWXYP30 
