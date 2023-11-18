
def lst_maker(string):
    str_lst=list(string)
    return str_lst

def int_maker_lst(lst):
    int_lst=[]
    for i in lst:
        int_lst.append(int(i))
    return int_lst    
        

def reverse_lst(lst):
    int_rev_credit_card_num=[]
    index=-1

    for i in lst:
        int_rev_credit_card_num.append(lst[index])
        index-=1
    return int_rev_credit_card_num


def multiple_lst(lst):
    rev_multiple_credit_card_num=[]
    index=0

    for i in lst:
        if index%2!=0:
            rev_multiple_credit_card_num.append(i*2)
        else:
            rev_multiple_credit_card_num.append(i)
        index+=1    
    return rev_multiple_credit_card_num            

def subract_lst(lst):
    rev_multiple_subtract_credit_card_num=[]
    for i in lst:
        if i>9:
            rev_multiple_subtract_credit_card_num.append(i-9)
        else:
            rev_multiple_subtract_credit_card_num.append(i)
    return rev_multiple_subtract_credit_card_num


def add_lst(lst):
    rev_multiple_subtract_add_credit_card_num=[]

    sum=0

    for i in lst:
        sum+=i
    return sum    















numbers_tuple=('0','1','2','3','4','5','6','7','8','9')



while True:
 


 credit_card_num=input('enter the credit card number: ')
 


 for i in credit_card_num:
     
     
     
     if i not in numbers_tuple:
         
         
         print('only numbers are acceptable!')
         break

 else:
          
          
          if len(credit_card_num)==16:
               
               
          

               if add_lst(subract_lst(multiple_lst(reverse_lst(int_maker_lst(lst_maker(credit_card_num))))))%10==0:


                
                
                   

            
            
                 print('Valid')
                 break
               else:

                
               
            
               
                 print('invalid')
                 break
             
          else:
              
              print('the credit card number lenght must be 16!')
      
