
def CLDVal (locList_List):
     global genStop , L_ErrParameters , N_Errs

     genStop = 0
     L_ErrParameters = []
     N_Errs = 0

     for L_list in locList_List :
          if (L_list[1]>=L_list[2] and L_list[1]<=L_list[3]) :
               print("OK")
          else :
               print("NOK")
               genStop = 1
               N_Errs += 1
               L_ErrParameters += [L_list[0]]         


