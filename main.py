from tkinter import *
from tkinter import messagebox
import random

billnumber=random.randint(500,1000)
def bill_area():
    #if nameEntry.get()=='' or phoneEntry.get()=='':
   #     messagebox.showerror('Error','Customer Details are Required')
   # elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
   #     messagebox.showerror('Error','No Products are selected')
   # elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
   #     messagebox.showerror('Error','No Products are selected')
        textarea.delete(1.0, END)
        textarea.insert(END, '\t\t** Welcome Customer **\n')
        textarea.insert(END, f'\nBill Number: {billnumber}\n')
        textarea.insert(END, f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END, f'\nPhone Number: {phoneEntry.get()}\n')
        textarea.insert(END, '\n============================================================')
        textarea.insert(END, '  Product\t\t\tQuantity\t\t\tPrice')
        textarea.insert(END, '\n============================================================')
        # Cosmetics Prices
        if bathsoapEntry.get() != '0':
            textarea.insert(END, f'\n  Bath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice} Rs')
        if facecreamEntry.get() != '0':
            textarea.insert(END, f'\n  Face Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
        if facewashEntry.get() != '0':
            textarea.insert(END, f'\n  Face Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
        if hairsprayEntry.get() != '0':
            textarea.insert(END, f'\n  Hair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
        if hairgelEntry.get() != '0':
            textarea.insert(END, f'\n  Hair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
        if bodylotionEntry.get() != '0':
            textarea.insert(END, f'\n  Body Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')

        # Grocery Prices
        if riceEntry.get() != '0':
            textarea.insert(END, f'\n  Rice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
        if daalEntry.get() != '0':
            textarea.insert(END, f'\n  Daal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
        if oilEntry.get() != '0':
            textarea.insert(END, f'\n  Oil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')
        if sugarEntry.get() != '0':
            textarea.insert(END, f'\n  Sugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
        if teaEntry.get() != '0':
            textarea.insert(END, f'\n  Tea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
        if wheatEntry.get() != '0':
            textarea.insert(END, f'\n  Wheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')

        # Drinks Prices
        if fantaEntry.get() != '0':
            textarea.insert(END, f'\n  Fanta\t\t\t{fantaEntry.get()}\t\t\t{fantaprice} Rs')
        if PepsiEntry.get() != '0':
            textarea.insert(END, f'\n  Pepsi\t\t\t{PepsiEntry.get()}\t\t\t{Pepsiprice} Rs')
        if spriteEntry.get() != '0':
            textarea.insert(END, f'\n  Sprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
        if redbullEntry.get() != '0':
            textarea.insert(END, f'\n  Red Bull\t\t\t{redbullEntry.get()}\t\t\t{redbullprice} Rs')
        if frootiEntry.get() != '0':
            textarea.insert(END, f'\n  Frooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
        if cococolaEntry.get() != '0':
            textarea.insert(END, f'\n  Coco Cola\t\t\t{cococolaEntry.get()}\t\t\t{cococolaprice} Rs')

        textarea.insert(END, '\n------------------------------------------------------------')

        # taxbill
        if cosmetictaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\n  Cosmetic Tax\t\t\t\t{cosmetictaxEntry.get()} Rs')
        if grocerytaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\n  Grocery Tax\t\t\t\t{grocerytaxEntry.get()} Rs')
        if drinkstaxEntry.get() != '0.0 Rs':
            textarea.insert(END, f'\n  Drinks Tax\t\t\t\t{drinkstaxEntry.get()} Rs')

        textarea.insert(END, '\n------------------------------------------------------------')
        textarea.insert(END, f'\n  Total Bill \t\t\t\t{totalbill} Rs')
        textarea.insert(END, '\n------------------------------------------------------------')




def total():
   global soapprice,facecreamprice,facewashprice,hairsprayprice,hairgelprice,bodylotionprice
   global riceprice,daalprice,oilprice,sugarprice,teaprice,wheatprice
   global fantaprice,Pepsiprice,spriteprice,redbullprice,frootiprice,cococolaprice
   global totalbill
    #cosmetic price
   soapprice=int(bathsoapEntry.get())* 20
   facecreamprice=int(facecreamEntry.get())*50
   facewashprice = int(facewashEntry.get()) * 40
   hairsprayprice = int(hairsprayEntry.get()) * 60
   hairgelprice = int(hairgelEntry.get()) * 45
   bodylotionprice = int(bodylotionEntry.get()) *70

   totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
   cosmeticpriceEntry.delete(0,END)
   cosmeticpriceEntry.insert(0,f'{totalcosmeticprice} Rs')
   cosmetictax=totalcosmeticprice*0.12
   cosmetictaxEntry.delete(0,END)
   cosmetictaxEntry.insert(0,str(cosmetictax)+'Rs')

   #grocery price
   riceprice=int(riceEntry.get())* 20
   daalprice = int(daalEntry.get()) * 30
   oilprice = int(oilEntry.get()) * 40
   sugarprice = int(sugarEntry.get()) * 60
   teaprice = int(teaEntry.get()) * 35
   wheatprice = int(wheatEntry.get()) * 65

   totalgroceryprice=riceprice+daalprice+oilprice+sugarprice+teaprice+wheatprice
   grocerypriceEntry.delete(0,END)
   grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
   grocerytax = totalgroceryprice * 0.12
   grocerytaxEntry.delete(0, END)
   grocerytaxEntry.insert(0, str(grocerytax) + 'Rs')

   #drinks price
   fantaprice=int(fantaEntry.get())*30
   Pepsiprice = int(PepsiEntry.get()) * 35
   spriteprice=int(spriteEntry.get())*37
   redbullprice=int(redbullEntry.get())*60
   frootiprice=int(frootiEntry.get())*40
   cococolaprice = int(cococolaEntry.get()) * 45

   totaldrinksprice=fantaprice+Pepsiprice+spriteprice+redbullprice+frootiprice+cococolaprice
   drinkspriceEntry.delete(0,END)
   drinkspriceEntry.insert(0,f'{totaldrinksprice} Rs')
   drinkstax = totaldrinksprice * 0.12
   drinkstaxEntry.delete(0, END)
   drinkstaxEntry.insert(0, str(drinkstax) + 'Rs')

   #total bill
   totalbill=totalcosmeticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax

root=Tk()
root.title('Retail Billing System')
root.geometry('1290x685')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                   ,bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold')
                                  ,fg='gold',bd=8,relief=GROOVE,bg='gray20')
customer_details_frame.pack(fill=X,pady=10)

nameLabel=Label(customer_details_frame,text='Name',font=('times new roman',15,'bold')
                ,bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20,pady=2)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold')
                ,bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold')
                ,bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),
                          bg='grey20',fg='gold',bd=8,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),
                          bg='grey20',fg='gold',bd=8,relief=GROOVE)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)
daalEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Drinks',font=('times new roman',15,'bold'),
                          bg='grey20',fg='gold',bd=8,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

fantaLabel=Label(drinksFrame,text='Fanta',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
fantaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

fantaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fantaEntry.grid(row=0,column=1,pady=9,padx=10)
fantaEntry.insert(0,0)

PepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
PepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

PepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
PepsiEntry.grid(row=1,column=1,pady=9,padx=10)
PepsiEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

redbullLabel=Label(drinksFrame,text='Red Bull',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
redbullLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

redbullEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
redbullEntry.grid(row=3,column=1,pady=9,padx=10)
redbullEntry.insert(0,0)

frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)
frootiEntry.insert(0,0)

cococolaLabel=Label(drinksFrame,text='Coco Cola',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
cococolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cococolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)
cococolaEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)

billarealabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='gray20')
billmenuFrame.pack()

cosmeticpriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold') ,bg='gray20',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')
cosmeticpriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold') ,bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')
grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

drinkspriceLabel=Label(billmenuFrame,text='Cold Drink Price',font=('times new roman',14,'bold') ,bg='gray20',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')
drinkspriceEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmetictaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',15,'bold') ,bg='gray20',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')
cosmetictaxEntry=Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,pady=6,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roman',15,'bold') ,bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')
grocerytaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,pady=6,padx=10)

drinkstaxLabel=Label(billmenuFrame,text='Cold Drink Tax',font=('times new roman',15,'bold') ,bg='gray20',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')
drinkstaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=5)


root.mainloop()