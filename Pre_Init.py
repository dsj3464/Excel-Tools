#coding=gbk
import xlwings as xw
def Pre_Init(wb):
    sht=wb.sheets[0];
    rng=sht.range("A1").expand("down").value
    if rng==None: #rng=None ����ĸ��û�и�ʽ
        col_num=0
        l=0
    else: #ĸ���и�ʽ
        l=len(rng)
        if  isinstance(rng, str) is True:
            l=1
        right_rng=sht.range((l,1)).expand("right").value
        col_num = len(right_rng)  # �и�����
        if isinstance(right_rng,str):
            col_num=1

    return col_num,l+1
