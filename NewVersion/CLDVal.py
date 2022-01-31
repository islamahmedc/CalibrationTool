
def CLDVal (li):
     global genStop , L_ErrParameters , CLD_List
     CLD_List = li
     genStop = 0
     L_ErrParameters = []
     N_Errs = 0

     for L_list in CLD_List :
          if (float(L_list[1]) >= float(L_list[2]) and float(L_list[1]) <= float(L_list[3])) :
               print("OK")
          else :
               print("NOK")
               genStop = 1
               N_Errs += 1
               L_ErrParameters += [L_list[0]] 
      


