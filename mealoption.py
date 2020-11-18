meal=[]                                     #宣告一個空陣列(儲存菜單的陣列)
while(True):                                #針對選擇做設計
    key=input("請輸入你的操作行為:(1).新增餐點 (2).刪除餐點 (3).按q離開\n")        #key作為選擇的輸入鍵
    if(key=="1"):
        addmeal=input("請輸入你要新增的餐點:")                                   #addmeal為新增餐點的輸入方式
        meal.append(addmeal)
        print(meal)                                                            #輸入完後印出所有餐點
    elif(key =="2"):                                    
        if(len(meal)==0):                                                      #判定菜單有沒有東西
            print("目前沒有餐點")
        else:                                                                  #如果有
            print(meal)                                                        #印出菜單
            deletemeal=input("請輸入你要刪除的餐點:")                            #deletemeal為刪除餐點的輸入方式
            if(deletemeal in meal):
                meal.remove(deletemeal)                                        #移除meal內的菜單
                print(meal)                                                    #印出菜單 
            else:
                print("沒有此餐點")                                             #判定輸入完的菜單後，能否找到，找不到告知此訊息
    elif(key=="q"):                                                            #按q離開
        break
    else:                                                                      #操作失敗請重新輸入
        print("沒有此操作，請重新輸入")