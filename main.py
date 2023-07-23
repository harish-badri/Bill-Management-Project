from tkinter import *

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

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)

facewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),
                          bg='grey20',fg='gold',bd=8,relief=GROOVE)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)

oilLabel=Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,pady=9,padx=10)

daalLabel=Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

daalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=2,column=1,pady=9,padx=10)

wheatLabel=Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=3,column=1,pady=9,padx=10)

sugarLabel=Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)

teaLabel=Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,pady=9,padx=10)

drinksFrame=LabelFrame(productsFrame,text='Drinks',font=('times new roman',15,'bold'),
                          bg='grey20',fg='gold',bd=8,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

fantaLabel=Label(drinksFrame,text='Fanta',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
fantaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

fantaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
fantaEntry.grid(row=0,column=1,pady=9,padx=10)

PepsiLabel=Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
PepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

PepsiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
PepsiEntry.grid(row=1,column=1,pady=9,padx=10)

spriteLabel=Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,pady=9,padx=10)

redbullLabel=Label(drinksFrame,text='Red Bull',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
redbullLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

redbullEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
redbullEntry.grid(row=3,column=1,pady=9,padx=10)

frootiLabel=Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=4,column=1,pady=9,padx=10)

cococolaLabel=Label(drinksFrame,text='Coco Cola',font=('times new roman',15,'bold'),
                    bg='grey20',fg='white')
cococolaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cococolaEntry=Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cococolaEntry.grid(row=5,column=1,pady=9,padx=10)

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

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=5)


root.mainloop()