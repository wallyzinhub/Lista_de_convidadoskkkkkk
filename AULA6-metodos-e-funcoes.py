def tem_sete_items(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False



if tem_sete_items({1,2,3,4,5,6,7,8}):
    print("realmente tem sete items")