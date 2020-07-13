from tkinter import *
from tkinter import ttk
import random
import time
import datetime

root=Tk()
root.geometry("1350x650+0+0")
root.title("foody order sysytem")
root.configure(background="black")
def Exit():
    qExit=messagebox.askyesno("ordering system","Do you want to exit the system")
    if qExit > 0:
        root.destroy()
        return
def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
   
    CostofDelivery.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    TimeOfOrder.set("")
    DateOfOrder.set("")
def OrderRef():
    Refpay=random.randint(10500,709467)
    Refpaid=("MC"+str(Refpay))
    CustomerRef.set(Refpaid)
def CostofOrder():
    Qty1=float(QtyWhiteWine.get())
    Qty2=float(QtyRedWine.get())
    Qty3=float(QtyOtherWine.get())

    UnitPrice1=float(UnitPriceWhiteWine.get())
    UnitPrice2=float(UnitPriceRedWine.get())
    UnitPrice3=float(UnitPriceOtherWine.get())

    CostofWine1="$",str("%.2f"%(Qty1*UnitPrice1))
    CostofWine2="$",str("%.2f"%(Qty1*UnitPrice2))
    CostofWine3="$",str("%.2f"%(Qty1*UnitPrice3))

    CostofWhiteWine.set(CostofWine1)
    CostofRedWine.set(CostofWine2)
    CostofOtherWine.set(CostofWine3)

    CostWine1=(Qty1*UnitPrice1)
    CostWine2=(Qty1*UnitPrice2)
    CostWine3=(Qty1*UnitPrice3)

    AllCost=((Qty1*UnitPrice1)+(Qty2*UnitPrice2)+(Qty3*UnitPrice3))
    TaxAll="$",str("%.2f"%((AllCost)*0.02))
    Tax.set(TaxAll)
    SubTotalp="$",str("%.2f"%(AllCost))
    SubTotal.set(SubTotalp)
    TotalCostp="$",str("%.2f"%(AllCost+((AllCost)*0.02)))
    TotalCost.set(TotalCostp)
    return

#======================Variable===================================

CustomerRef=StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
CostofWhiteWine=StringVar()
CostofRedWine=StringVar()
CostofOtherWine=StringVar()
CostofDelivery=StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
CustomerEmail=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()
Discount=StringVar()
CostofWhiteWine=StringVar()
CostofRedWine=StringVar()
CostofOtherWine=StringVar()
UnitPriceOtherWine=StringVar()
UnitPriceRedWine=StringVar()
UnitPriceWhiteWine=StringVar()
QtyOtherWine=StringVar()
QtyRedWine=StringVar()
QtyWhiteWine=StringVar()
#Discount=StringVar()
#===============================init component========================================

CostofWhiteWine.set(0)
CostofRedWine.set(0)
CostofOtherWine.set(0)    
CostofWhiteWine.set(0)
CostofRedWine.set(0)
CostofOtherWine.set(0)
UnitPriceOtherWine.set(0)
UnitPriceRedWine.set(0)
UnitPriceWhiteWine.set(0)
QtyOtherWine.set(0)
QtyRedWine.set(0)
QtyWhiteWine.set(0)
Discount.set(0)

TimeOfOrder.set(time.strftime("%H:%M:%S"))# Time
DateOfOrder.set(time.strftime("%d/%m/%y"))# Date
#==============================Frames==================================
Tops=Frame(root,width=1350,height=50,bd=16,relief="raise")
Tops.pack(side=TOP)
LF=Frame(root,width=700,height=650,bd=16,relief="raise")
LF.pack(side=LEFT)
RF=Frame(root,width=600,height=650,bd=16,relief="raise")
RF.pack(side=RIGHT)
Tops.configure(background="black")
LF.configure(background="black")
RF.configure(background="black")
LeftInsideLF=Frame(LF, width=700 ,height=100,bd=8,relief="raise")
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF=Frame(LF, width=700 ,height=400,bd=8,relief="raise")
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF=Frame(RF, width=604 ,height=200,bd=8,relief="raise")
RightInsideLF.pack(side=TOP)
RightInsideLFLF=Frame(RF, width=306 ,height=400,bd=8,relief="raise")
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF=Frame(RF, width=300 ,height=400,bd=8,relief="raise")
RightInsideRFRF.pack(side=RIGHT)
#===========================ProjectTitle================================
lblInfo=Label(Tops,font=("arial",50,'bold'),text="     Online Ordering System         ",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)
#===============================Top Left Frame====================
lblCustomerName=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Name",
                     fg="black",bd=10,anchor="w")
lblCustomerName.grid(row=0,column=0)
txtCustomerName=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=45,
                  bg="white",justify="left",textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)

lblCustomerPhone=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Phone",
                     fg="black",bd=10,anchor="w")
lblCustomerPhone.grid(row=1,column=0)
txtCustomerPhone=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=45,
                  bg="white",justify="left",textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1,column=1)

lblCustomerEmail=Label(LeftInsideLF,font=('arial',14,'bold'),text="Customer Email",
                     fg="black",bd=10,anchor="w")
lblCustomerEmail.grid(row=2,column=0)
txtCustomerEmail=Entry(LeftInsideLF,font=('arial',14,'bold'),bd=20,width=45,
                  bg="white",justify="left",textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)





#===============================Top Right Frame===================
lblDateofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Date of order",
                     fg="black",bd=10,anchor="w")
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=35,
                  bg="white",justify="left",textvariable=DateOfOrder)
txtDateofOrder.grid(row=0,column=1)

lblTimeofOrder=Label(RightInsideLF,font=('arial',12,'bold'),text="Time of order",
                     fg="black",bd=10,anchor="w")
lblTimeofOrder.grid(row=1,column=0)
txtTimeofOrder=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=35,
                  bg="white",justify="left",textvariable=TimeOfOrder)
txtTimeofOrder.grid(row=1,column=1)

lblCustomerRef=Label(RightInsideLF,font=('arial',12,'bold'),text="Customer Ref",
                     fg="black",bd=10,anchor="w")
lblCustomerRef.grid(row=2,column=0)
txtCustomerRef=Entry(RightInsideLF,font=('arial',12,'bold'),bd=20,width=35,
                  bg="white",justify="left",textvariable=CustomerRef)
txtCustomerRef.grid(row=2,column=1)

#=================================Bottom Right Frame========================
lblMethodOfPayment=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Methoad of Payment',
                          fg="black",bd=16,anchor="w")
lblMethodOfPayment.grid(row=0,column=0)
cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF,font=('arial',10,'bold'))
cmdMethodOfPayment['value']=('','Cash','Debit Card','Visa Card','Master Card')
cmdMethodOfPayment.grid(row=0,column=1)
lblDiscount=Label(RightInsideLFLF,font=('arial',12,'bold'),text='Discount',
                  fg='black',bd=16,anchor='w')
lblDiscount.grid(row=1,column=0)
txtDiscount=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                  bg="white",justify="left",textvariable=Discount)
txtDiscount.grid(row=1,column=1)
lblTax=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Tax",
             fg="black",bd=16,anchor='w')
lblTax.grid(row=2,column=0)
txtTax=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
             bg="white",justify='left',textvariable=Tax)
txtTax.grid(row=2,column=1)
lblSubTotal=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Sub Total ",
                  fg="black",bd=16,anchor="w")
lblSubTotal.grid(row=3,column=0)
txtSubTotal=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                  bg="white",justify='left',textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)

lblTotalCost=Label(RightInsideLFLF,font=('arial',12,'bold'),text="Total Cost",
             fg="black",bd=16,anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost=Entry(RightInsideLFLF,font=('arial',12,'bold'),bd=16,width=18,
                  bg="white",justify='left',textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1)

#========================buttons Left Frame=========================
lblItemOrder=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Item Order',fg="black",bd=20)
lblItemOrder.grid(row=0,column=0)
lblQty=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Quantity',fg="black",bd=10)
lblQty.grid(row=0,column=1)
lblUnitPrice=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Unit Price',fg="black",bd=20)
lblUnitPrice.grid(row=0,column=2)
lblCostofItem=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Cost of Item',fg="black",bd=20)
lblCostofItem.grid(row=0,column=3)
#============
lblWhiteWine=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='White Wine',fg="black",bd=20)
lblWhiteWine.grid(row=1,column=0)
lblRedWine=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Red Wine',fg="black",bd=20)
lblRedWine.grid(row=2,column=0)
lblOtherWine=Label(LeftInsideLFLF,font=('arial',14,'bold'),text='Other Wine',fg="black",bd=20)
lblOtherWine.grid(row=3,column=0)
#==============
txtQtyWhiteWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=17,
                  bg="white",justify='left',textvariable=QtyWhiteWine)
txtQtyWhiteWine.grid(row=1,column=1)
txtQtyRedWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=QtyRedWine)
txtQtyRedWine.grid(row=2,column=1)
txtQtyOtherWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=QtyOtherWine)
txtQtyOtherWine.grid(row=3,column=1)
#======================
txtUnitPriceWhiteWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=UnitPriceWhiteWine)
txtUnitPriceWhiteWine.grid(row=1,column=2)
txtUnitPriceRedWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=UnitPriceRedWine)
txtUnitPriceRedWine.grid(row=2,column=2)

txtUnitPriceOtherWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=UnitPriceOtherWine)
txtUnitPriceOtherWine.grid(row=3,column=2)
#=======================================================================
txtCostofWhiteWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=CostofWhiteWine)
txtCostofWhiteWine.grid(row=1,column=3)
txtCostofRedWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=CostofRedWine)
txtCostofRedWine.grid(row=2,column=3)
txtCostofOtherWine=Entry(LeftInsideLFLF,font=('arial',12,'bold'),bd=20,width=16,
                  bg="white",justify='left',textvariable=CostofOtherWine)
txtCostofOtherWine.grid(row=3,column=3)
#==============================Buttons Right Frame------------------
btnDiscount=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',11,'bold'),width=7,
                    text="Discount",bg='white',command=CostofOrder).grid(row=0,column=0)

btnTotalCost=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',11,'bold'),width=7,
                    text="TotalCost",bg='white',command=CostofOrder).grid(row=0,column=0)

btnReset=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',12,'bold'),width=7,
                    text="Reset",bg='white',command=Reset).grid(row=1,column=0)
btnOderRef=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',12,'bold'),width=7,
                    text="OderRef",bg='white',command=OrderRef).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF,pady=8,fg="black",font=('arial',12,'bold'),width=7,
               text="Exit",bg='white',command=Exit).grid(row=3,column=0)
root.mainloop()

