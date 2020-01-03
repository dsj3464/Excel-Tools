from Add_Modify import  *
def sub_table_solve(mem_map,sub_wb,row_start,col_num,key,need_add_col):
    # ��sub_wb������ݴ浽/�޶���mem_map��
    sht=sub_wb.sheets[0]
    rng=sht.range(row_start,key).expand('down').value
    size=len(rng)

    rng=sht.range((row_start,1),(row_start+size-1,col_num)).value
    for sub_rng in rng:
        std_handle(li=sub_rng, key=key)
        #
        #�ɼ��еĴ���
        if sub_rng[key-1] in mem_map :
            map_modify(mem_map=mem_map,lis=sub_rng,key=key,need_add_col=need_add_col)
        else:
            map_add(mem_map=mem_map,li=sub_rng,key=key)

    return