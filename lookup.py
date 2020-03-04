# coding=gbk

#�淶�����
def check(a,b,c,d):
    if len(a)!=len(b):
        return 1
    elif len(c)!=len(d):
        return 2
    return 0

#��һ��������б�׼������
#ȫ��ת��Ϊ�ַ���������ȥ�ո�
def std_handle(rng):
    for i in range(0,len(rng)):
        ele=rng[i]
        if (isinstance(ele, str)):
            rng[i] = ele.replace(' ','')
        elif (isinstance(ele, float)):
            if (int(ele) == ele):
                rng[i] = str(int(ele))
            else:
                rng[i] = str(ele)

    return

# ����C���롾A������ƥ�䣬������Ӧ��B�����е�ֵ��Ϊ������롾D����
def lookup(wb,A,B,C,D):
    sht=wb.sheets[0]
    A_rng=sht.range(A).expand('down').value
    std_handle(A_rng)
    B_rng=sht.range(B).expand('down').value
    std_handle(B_rng)
    C_rng=sht.range(C).expand('down').value
    std_handle(C_rng)
    D_rng=list()

    err = check(A_rng, B_rng, C_rng, D_rng)
    if err == 1:
        print('A,B�����С��һ��')
        return
    elif err == 2:
        print('C,D��С��һ��')
        return

    for c in C_rng:
            flag=0
            for i in range(0,len(A_rng)):
                a = A_rng[i]
                if c==a:
                    flag=1
                    D_rng.append(B_rng[i])
                    break

            if flag==0:
                D_rng.append('None')

    sht.range(D).options(transpose=True).value=D_rng
    return

#�ֱ�ƥ��  ����AB��CD����ͬһ���ļ���
def lookup(wb1,wb2,A,B,C,D):
    sht1=wb1.sheets[0]
    sht2=wb2.sheets[0]
    A_rng = sht1.range(A).expand('down').value
    std_handle(A_rng)
    B_rng = sht1.range(B).expand('down').value
    std_handle(B_rng)
    C_rng = sht2.range(C).expand('down').value
    std_handle(C_rng)
    D_rng = list()

    err=check(A_rng,B_rng,C_rng,D_rng)
    if err==1:
        print('A,B�����С��һ��')
        return
    elif err==2:
        print('C,D��С��һ��')
        return

    for c in C_rng:
        flag=0
        for i in range(0,len(A_rng)):
            a = A_rng[i]
            if c==a:
                flag=1
                D_rng.append(B_rng[i])
                break

        if flag==0:
            D_rng.append('None')

    sht2.range(D).options(transpose=True).value = D_rng
    return

# import xlwings as xl
# try:
#     app = xl.App(visible=False)
#     wb = app.books.open(r'C:\Users\DSJ\Desktop\test.xlsx')
#     A = 'A2:A8'
#     B = 'B2:B8'
#     C = 'C2:C4'
#     D = 'D2:D4'
#     lookup(wb, A, B, C, D)
#     wb.save()
#     wb.close()
# finally:
#     app.quit()