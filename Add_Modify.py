#coding=gbk
import copy

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def std_handle(li, key):
    value = li[key - 1]
    if (isinstance(value, str)):
        li[key-1]=value.replace(' ','')
    elif (isinstance(value, float)):
        if (int(value) == value):
            li[key - 1] = str(int(value))
        else:
            li[key - 1] = str(value)

    return


def map_add(mem_map, li, key):
    mem_map[li[key - 1]] = []
    mem_map[li[key - 1]] = copy.deepcopy(li)
    print(mem_map)
    return


def map_modify(mem_map, lis, key,need_add_col):
    # mem_map��һ���ֵ䣬list���б�key��ʾ��һ������Ϊ��ֵ��
    key_value = lis[key - 1]
    length = len(lis)

    #���п���Ϊ�ַ����Ŀɼ���ת��Ϊ����
    for c in need_add_col:
        if lis[c-1] is None:
            continue
        if is_number(lis[c-1]) == False:
            print('�ɼ����������')
            raise SystemExit
        if isinstance(lis[c-1],str):
            lis[c-1]=float(lis[c-1].replace(' ',''))

    for i in range(length):
        if (i == key - 1):
            continue
        if (mem_map[key_value][i] == None):
            mem_map[key_value][i] = copy.deepcopy(lis[i])

        # elif i+1 in tuple
        elif (i+1 in need_add_col):
            mem_map[key_value][i] = lis[i] + mem_map[key_value][i]

    print(mem_map)
    return