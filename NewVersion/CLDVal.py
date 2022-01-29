def CLDVal (locList_List):
   global genStop
   global L_ErrParameters
   global N_Errs

   for L_list in locList_List :
       if (L_list[1]>=L_list[2] and L_list[1]<=L_list[3]) :
            print("OK")
       else :
            genStop = 1
            N_Errs += 1
            L_ErrParameters += [L_list[0]]


