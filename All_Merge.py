#�ϲ����б�map��
#coding=gbk
from Sub_Table_Solve import *
from  Map_Write import *
import xlwings as xw
def all_merge(mem_map,wb,file_name_list,row_start,col_num,key,need_add_col):
    for file_name in file_name_list:
        # �����ļ�
        print('���ļ�:'+file_name)
        try:
            app=xw.App(visible=False)
            sub_wb=app.books.open(file_name)
            # ���ļ�����
            sub_table_solve(mem_map=mem_map,sub_wb=sub_wb,row_start=row_start,col_num=col_num,key=key,need_add_col=need_add_col)
        finally:
            #�ر����ļ�
            print(file_name+'�������')
            sub_wb.save()
            sub_wb.close()
            app.quit()
            app.kill()
    # ��map�е�����д��excel
    map_write(mem_map=mem_map,wb=wb,row_start=row_start,col_num=col_num)
    return