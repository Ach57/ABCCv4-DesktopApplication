import gspread
import tkinter as tk
from tkinter import ttk, StringVar, Toplevel
from PIL import Image, ImageTk
from datetime import date, timedelta
import matplotlib.pyplot as plt
from tkinter.filedialog import askdirectory
from tkinter import messagebox
import matplotlib.pyplot as plt
import logging


#Constants:
Font_tuple=("Consolas Bold Italic",30,'bold')
Font_tuple1=("Consolas Bold Italic",12,'bold')
Font_tuple2=("Consolas",12,'bold')
Font_tuple3=("Consolas",10,'bold')

fileName="C:\\Users\\admin\\Downloads\\Python_Project\\credentialsfile.json"
today=date.today()
#fileName=os.path.abspath('credentialsfile.json')
Logo='C:\\Users\\admin\\Downloads\\LOGO.ico'
#Logo=os.path.abspath('LOGO.ico')
bztFcqDi1Gy='C:\\Users\\admin\\Downloads\\Python_Project\\App_dev\\_bztFcqDi1Gy.png'
#bztFcqDi1Gy=os.path.abspath('_bztFcqDi1Gy.png')
downloadICon="C:\\Users\\admin\\Downloads\\DownloadIcon.png"
#downloadICon=os.path.abspath('DownloadIcon.png')
JpgLogo='C:\\Users\\admin\\Downloads\\JpgLogo.png'
#JpgLogo=os.path.abspath('JpgLogo.png')
SubmitIcon='C:\\Users\\admin\\Downloads\\SubmitIcon.png'
#SubmitIcon=os.path.abspath('SubmitIcon.png')
DeleteIcon='C:\\Users\\admin\\Downloads\\DeleteIcon.jpg'
#DeleteIcon=os.path.abspath('DeleteIcon.jpg')
StatusIcon='C:\\Users\\admin\\Downloads\\StatusIcon.png'
#StatusIcon=os.path.abspath('StatusIcon.png')
InventoryIcon="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\Inventory.png"
InventoryMangIcon="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\InventoryMang.jpg"
MiniDeleteIcon="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\Delete.png"
DeleteALL="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\DeleteAll.png"
DataImg="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\DATA.png"
InstructionIMG="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\Instructions.png"
UpdateImg="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\Update.png"
RepImg="C:\\Users\\admin\\Downloads\\Python_Project\\Machine learning\\Replacement.png"


my_img=Image.open(bztFcqDi1Gy)
resize_img=my_img.resize((620,140),Image.Resampling.LANCZOS)

my_img3=Image.open(SubmitIcon)
resize_my_img3=my_img3.resize((40,20),Image.Resampling.LANCZOS)

my_img4=Image.open(DeleteIcon)
resize_my_img4=my_img4.resize((40,20),Image.Resampling.LANCZOS)

my_img5=Image.open(StatusIcon)
resize_my_img5=my_img5.resize((80,25),Image.Resampling.LANCZOS)

my_img6=Image.open(InventoryIcon)
resize_my_img6=my_img6.resize((80,30),Image.Resampling.LANCZOS)

my_img7=Image.open(InventoryMangIcon)
resize_my_img7=my_img7.resize((500,140),Image.Resampling.LANCZOS)

my_img8=Image.open(MiniDeleteIcon)
resize_my_img8=my_img8.resize((60,15),Image.Resampling.LANCZOS)

my_img9=Image.open(DeleteALL)
resize_my_img9=my_img9.resize((30,10),Image.Resampling.LANCZOS)

my_img10=Image.open(DataImg)
resize_my_img10=my_img10.resize((50,25),Image.Resampling.LANCZOS)

my_img11=Image.open(InstructionIMG)
resize_my_img11=my_img11.resize((50,25),Image.Resampling.LANCZOS)

my_img12=Image.open(UpdateImg)
resize_my_img12=my_img12.resize((500,140),Image.Resampling.LANCZOS)

my_img13=Image.open(RepImg)
resize_my_img13=my_img13.resize((80,30),Image.Resampling.LANCZOS)

#Gspread:
sa=gspread.service_account(filename=fileName)
InventorySheet=sa.open("A&B Crystal Collection Inventory")
Transaction_tracker=InventorySheet.worksheet("Transaction tracker")
IssueTrackerSheet=sa.open("Issues Tracker")
Replacement_Tracker=IssueTrackerSheet.worksheet("Raj's Replacement Tracker")

Names=["","Achraf C","Aymen C","Lakesh","Khouloud","Mohamed B","Wissem B","Achour A"]
BatchList=list()
Name=""
txt=""
BATCHES_ISSUE=dict()
logging.basicConfig(filename="InventoryIssueReplacmeent tracker.log",filemode='a',format='%(asctime)s %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.critical('(LOGIN) Sucessfully logged in')


def Issue_getter(worksheet):
        FailedQc=worksheet.findall('Failed QC')
        FailedQc_copy = FailedQc.copy()
        FailedQc.clear()
        for element in FailedQc_copy:
                x=worksheet.acell('V{}'.format(element.row)).value
                if x!="Waiting for other lines from Issue tracker":
                        FailedQc.append(x)
        return len(FailedQc)

class IssueConverter:
              
        Issues=["Missing Text","Wrong converted picture",
                "Poor quality picture","Wrong text","Missing File",
                "No picture available","Full cancellation",
                "Read Me file not respected","Too small in the crystal",
                "Wrong converted dimensions","Track Shipment"]
        Convert=["Sent to conversion: Redo Old Picture (check comments)",
                "Sent to conversion: Redo Old Picture (check comments)",
                "Sent to customer service",
                "Sent to conversion: Redo Old Picture (check comments)",
                "Sent to conversion: Redo Old Picture (check comments)",
                "Sent to customer service","Closed: refunded",
                "Sent to Batching","Sent to conversion: Redo Old Picture (check comments)",
                "Sent to Batching","Sent to Batching"]
        def DictCreator(Issues,Convert):
                myDict=dict()
                for i in range(11):
                        myDict[Issues[i]]=Convert[i]
                return myDict    
        IssueDict=DictCreator(Issues,Convert)
        
        def __init__(self,IssueEntered=str) -> None:

                self.IssueEntered=IssueEntered
        def Main(self,)->str:
            try:
                return self.IssueDict[self.IssueEntered]
            except KeyError:
                return "Unknown identifer"

class DataIssueTrackerCleansing(IssueConverter): 
    
    def orgin_getter(self,worksheet,orderId):
        return str(worksheet.acell('AM{}'.format(worksheet.find(orderId).row)).value)

    def list_element_switch(self,ll=list,index1=int,index2=int):
        #User gives index1 and index2
        #Return is to switch index1 with index2 and veverse
        #ll=["a","b","c","d","e"] list_element_switch(ll,1,3) -> ["a","d","c","d","b","e"]
        copy,copy1=ll[index1],ll[index2]
        ll[index1],ll[index2]=copy1,copy
        return ll
    TupleOfUnwantedStuff=('LED Base',"Cleaning Kit",'Gift Card','Bag')
    def DataAssumbling(self,ll,ll_,BatchTracker)-> list:
        for j in range(2):
            ll[0].pop(4)
        if not(ll[0][2] in self.TupleOfUnwantedStuff):
            #elements=(str(today),'Production',self.orgin_getter(Batch_Tracker,ll[0][3]))  
            elements=(str(today),'Production',self.orgin_getter(BatchTracker,ll[0][3]))
            for i in range(3):
                ll[0].insert(i,elements[i])
            ll_copy=self.list_element_switch(ll[0],3,4)
            ll[0]=ll_copy
            if len(ll_[0])==1:
                element_=(ll_[0][0],"")
                for p in range(2):
                    ll[0].insert(5+p,element_[p])
            else:
                for p in range(2):
                    ll [0].insert(5+p,ll_[0][p])
            ll[0].insert(7,IssueConverter(ll[0][5]).Main()) 
            return ll
     
    def __init__(self, AToGList,VToWList,Batch_Tracker):
            self.AToGList=AToGList
            self.VToWList=VToWList
            self.Batch_Tracker=Batch_Tracker  
                 
    def Main(self,)-> list:
        return self.DataAssumbling(self.AToGList,self.VToWList,self.Batch_Tracker)          

class IssueTrackerUpdateClass(DataIssueTrackerCleansing):
    
    def FindingLastRow(self,):
            ri=next_available_row(Replacement_Tracker,1)
            FilterList=list(filter(None,Replacement_Tracker.row_values(ri)))
            if FilterList[-1]!=str(0):Replacement_Tracker.update('B{}'.format(ri),str(today));return ri+1
            else:return ri              
    
    def FailedQcGetter(self,BATCHES_ISSUE=dict):
        FailedQCList=list()
        for BATCH,n in BATCHES_ISSUE.items():
                BatchTracker=sa.open(BATCH).worksheet('Batch tracker')
                FailedQcs=BatchTracker.findall("Failed QC")
                for i in FailedQcs:
                        AToGList=BatchTracker.get("A{0}:G{0}".format(i.row))
                        VToWList=BatchTracker.get("V{0}:W{0}".format(i.row))
                        result=DataIssueTrackerCleansing(AToGList,VToWList,BatchTracker).Main()
                        if result!=None: FailedQCList.extend(result)
        return FailedQCList
    
    def FailedQCUpdater(self,FailedQCList):
            ReturnedRi=self.FindingLastRow()
            IssueList0=list()
            IssueList1=list()
            for issue in FailedQCList:IssueList0.append(issue[0:8]);IssueList1.append(issue[8:len(issue)])
            tupleofelement=(('B','I',IssueList0),('L','N',IssueList1))
            for minituple in tupleofelement:Replacement_Tracker.update('{0}{1}:{2}{3}'.format(minituple[0],ReturnedRi,minituple[1],len(IssueList0)+ReturnedRi),minituple[2])      
    def __init__(self, BATCHES_ISSUE=dict):
           self.BATCHES_ISSUE=BATCHES_ISSUE
    
    def Main(self,):
        self.FailedQCUpdater(self.FailedQcGetter(self.BATCHES_ISSUE))
                        


def next_available_row(worksheet,i):
    str_list = list(filter(None, worksheet.col_values(i)))
    return int(len(str_list)+1)
def next_row_by_element(worksheet,y,i):
    str_list=list(filter(lambda x: x==y,worksheet.col_values(i)))
    return str_list

def BatchChecker(batch=str)->bool:
    try:
        sa.open(batch)
        return True;
    except:
        return False;

class IssueInventoryApp(tk.Tk):
    #Inventory Functions:
    
    def InstructionFunction(self):
        messagebox.showinfo("Instructions","1-Enter the Batches\n\n2-Select your name\n\n3-Update Inventory.\n\nYou can review results or see charts!\n\t  Thank you!")
    
    def NameBatchescheck(self):
        global Name
        global BatchList
        if (len(BatchList)!=0 and Name!=""):
            self.InventoryUpdate.state(['!disabled'])
        
    def GetBatchFunction(self):
        global BatchList
        BatchEntered=self.BatchEntry.get()
        logging.error(f'(ENTRY) {BatchEntered} is entered')
        if (BatchChecker(BatchEntered)):
            if not(BatchEntered in BatchList):
                BatchList.append(BatchEntered)
                logging.error(f"(LOAD DATA) {BatchEntered} submitted")
                messagebox.showinfo("Update",f"{BatchEntered} has been successfully submitted!")
                self.deletebatch.state(["!disabled"])
                self.BatchEntry.delete(0,"end")
                self.BatchEntry.insert(0,"Enter a batch...")
                
            else:
                messagebox.showwarning("Warning",f"{BatchEntered} has already been submitted")
                logging.error(f'(WARNING) {BatchEntered} already existed')
            
        elif BatchEntered=="":
            logging.error('(DEBUG) User entered nothing')
            messagebox.showerror("Error","Nothing has been entered!")
        
        else:
            logging.error(f'(DEBUG) {BatchEntered} was not found')
            messagebox.showerror("Error",f"{BatchEntered} is unknown.\nPlease try again!")
    
    def Removeelementfunc(self):
        global BatchList
        global Question
        global LabelFrami
        global DeleteelementButton
        if self.clicked1.get() in BatchList:
            BatchList.remove("")
            logging.error(f'(DELOAD DATA) {self.clicked1.get()} is removed')
            BatchList.remove(self.clicked1.get())
            BatchList.insert(0,"")
            self.BatchMenu.grid_forget()
            self.clicked1.set("Select the batch...")
            self.BatchMenu=ttk.OptionMenu(LabelFrami,self.clicked1, *BatchList)
            self.BatchMenu.grid(row=1,column=0,columnspan=2)
            if (len(BatchList)==1):
                messagebox.showinfo("Update","All elements are delete")
                BatchList=list()
                logging.error(f'(LOAD DATA) All data is removed')
                self.deletebatch.state(['disabled'])
                Question.destroy()
        else:
            messagebox.showerror("Error","Please select from the list")
            
    def confirmButton(self):
        global Question
        global BatchList
        BatchList.remove("")
        Question.destroy()
            
    def DeleteCertainBatchesfunc(self):
        global BatchList
        global Question
        global LabelFrami
        global DeleteelementButton
        DeleteelementButton.state(['disabled'])
        self.clicked1= StringVar()
        BatchList.insert(0,"")
        self.clicked1.set("Select the batch...")
        self.BatchMenu=ttk.OptionMenu(LabelFrami,self.clicked1, *BatchList)
        self.BatchMenu.grid(row=1,column=0,columnspan=2)
        self.confirmbutton= ttk.Button(Question,text="Remove",command=self.Removeelementfunc)
        self.confirmbutton.pack()
        
        self.OkButton=ttk.Button(Question,text="Confirm",command=self.confirmButton)
        self.OkButton.pack()
        
    def DeleteAllFunc(self):
        global BatchList
        global Question
        BatchList=list()
        messagebox.showinfo("Update","All the entered batches are delete!")
        logging.error('(LOAD DATA) Data was completely erased')
        Question.destroy()
        self.deletebatch.state(['disabled'])
        self.BatchEntry.delete(0,"end")   
        self.BatchEntry.insert(0,"Enter the batch...")
        self.InventoryUpdate.state(['disabled'])
        
    def DeleteBatchesFunction(self):
        global Question
        global BatchList
        global LabelFrami
        global DeleteelementButton
        if len(BatchList)!=1:    
            Question=Toplevel()
            Question.iconbitmap(Logo)
            Question.title("Delete Batches")
            Label=ttk.Label(Question,text="\tWould you like to\ndelete batches or all of them?",
                            font=Font_tuple3,foreground="Red")
            Label.pack()
            
            LabelFrami=ttk.Labelframe(Question,)
            LabelFrami.pack()
            
            DeleteAllButton=ttk.Button(LabelFrami,text="Delete ALL",image=self.DeleteAllImg,
                                       compound=tk.LEFT, command=self.DeleteAllFunc)
            DeleteAllButton.grid(row=0,column=0,padx=10,pady=20)
            
            DeleteelementButton=ttk.Button(LabelFrami,text="Delete batches",image=self.DeleteAllImg,
                                           compound=tk.LEFT,command=self.DeleteCertainBatchesfunc)
            DeleteelementButton.grid(row=0,padx=10,column=1)
        else:
            messagebox.showinfo("Update",f'{BatchList[0]} is removed!')
            logging.error(f'(LOAD DATA) {BatchList[0]} was removed')
            BatchList=list()
            self.deletebatch.state(['disabled'])   
            self.BatchEntry.delete(0,"end")   
            self.BatchEntry.insert(0,"Enter the batch...")
            self.InventoryUpdate.state(['disabled'])
            
    '''Name getter and Name delete funtion:'''
    def NamegetterFunction(self):
        global Name
        if self.clicked.get() in Names and self.clicked.get()!="":
            Name=self.clicked.get()
            messagebox.showinfo("Update",f"Hello {Name}! Your name has been\n sucessfully submited!")
            self.deletename.state(["!disabled"])
            self.clicked.set(f"You've entered {Name}")
            logging.error(f'(NAME) {Name} entered ')
        else:
            messagebox.showwarning("Error","Please select a name from the list.\nOtherwise, add your name!")
            logging.error('(DEBUG INFORMATION) Entered name is invalid')
    def Namedeletefunction(self):
        global Name
        Name=''
        self.deletename.state(["disabled"])
        messagebox.showinfo("Update","Your name is erased!")
        logging.error('(DEBUG INFORMATION) Entered name is deleted')
        self.clicked.set("Select your name...")
        self.InventoryUpdate.state(['disabled'])
    '''-----------------------------------------'''
    def deleteEntry(self):
        self.BatchEntry.delete(0,"end")
    
    def statusinfo(self):
        global txt
        messagebox.showinfo("Update",txt)
        logging.error("(UPDATE) Status info")
     
    def GetChartFunc(self):
        '''
        InventoryDict=dict()
        for i in BatchList:
            if Transaction_tracker.findall(i)==[]:
                InventoryDict[i]=True
        ''' 
              
        
        
    def UpdateInventoryFunction(self):
        global Name
        global BatchList
        global txt
        
        txt=''
        
        for batch in BatchList:
            Batch_today=sa.open(batch)
            STOCK_REPLENISHMENT=Batch_today.worksheet("Stock Replenishment")
            BATCH_TRACKER=Batch_today.worksheet("Batch tracker")
            if next_row_by_element(Transaction_tracker,batch,2) == []:
                Last_row_Transaction_tracker=next_available_row(Transaction_tracker,1)
                Last_row_Stock_replenishment=next_available_row(STOCK_REPLENISHMENT,2)
            #Cleaning data:
                if STOCK_REPLENISHMENT.acell('A3').value==None:
                    y=next_available_row(BATCH_TRACKER,1)
                    ll=[[batch]]*(y-2)
                    BATCH_TRACKER.update("H2:H{}".format(y),ll)
                     
                STOCK=STOCK_REPLENISHMENT.get("A3:E{}".format(Last_row_Stock_replenishment))
                
                for element in STOCK:
                    element.insert(0,str(today))
                    element.append(Name)    
                Transaction_tracker.update("A{}:G{}".format(Last_row_Transaction_tracker,Last_row_Transaction_tracker+len(STOCK)),STOCK)     
                txt+=f"{batch} is updated!\n"
                logging.error("(UPATED) {} is updated".format(batch))
            else:
                txt+=f"{batch} was ALREADY updated!\n"
                logging.error("(DEBUG) {} is ALREADY updated".format(batch))
        self.StatusButton.state(["!disabled"])
        BatchList=list()
        Name=""
        self.deletebatch.state(['disabled'])
        self.deletename.state(['disabled'])
        self.InventoryUpdate.state(['disabled'])
        
    #Replacement Function:
    def ReplacementInst(self):
        messagebox.showinfo('Instruction',"1- Enter the batches\n2-Click on the Update button.\nYou can review charts and results.")
        
    def Enablebutton(self):
        global BATCHES_ISSUE
        if len(BATCHES_ISSUE)>0:
            self.UpdateReplacementButton.state(['!disabled'])
            self.ChartButtonRe.state(['!disabled'])
            
    def GetReplacementBatch(self):
        global BATCHES_ISSUE
        e=self.BatchReplacementEntry.get()
        logging.error(f"(ENTRY) {e} is submitted")
        try:
                BATCH = sa.open(e)
                Batch_tracker=BATCH.worksheet('Batch tracker')
                if e in BATCHES_ISSUE.keys():
                        messagebox.showerror("Error",'You already have entered "{}"'.format(e)) 
                else:
                        if Issue_getter(Batch_tracker)!=0:
                                num_of_issues=Issue_getter(Batch_tracker)
                                logging.error(f"(LOAD DATA) {e} is entered")
                                BATCHES_ISSUE[e]=num_of_issues
                                messagebox.showinfo(f'Update',f"{e} has been successfully added!")
                                self.deletebatchreplacement.state(['!disabled'])
                        else:
                            logging.error(f"(DEBUG) {e} has no issues")
                            messagebox.showerror("Error",f'{e} has no issue in it!')                 
        except:
            logging.error(f'(ERROR) {e} was not found')
            messagebox.showerror("Error","Could not find the file!")

        self.BatchReplacementEntry.delete(0,'end')
        self.BatchReplacementEntry.insert(0,"Enter the batch...")
        
    def deleteAllReplacementBatch(self):
        logging.error("(DELETE) All Batches are deleted")
        del BATCHES_ISSUE
        BATCHES_ISSUE=dict()
        Question1.destroy()
        self.UpdateReplacementButton.state(['disabled'])
        self.deletebatchreplacement.state(['disabled'])
        messagebox.showinfo("UPDATE","All batches have been deleted")
        
    def DeleteReplacementBatchfunc(self):
        global BATCHES_ISSUE
        global Question1
        global LabelFrami1
        if len(BATCHES_ISSUE.keys())==1:
            logging.error("(DELETE) Entered data is removed")
            messagebox.showinfo("Update",'The entered batch is removed!') #{'Copy of Batch 24062022': 6}
            BATCHES_ISSUE.popitem()
            self.deletebatchreplacement.state(['disabled'])
            self.BatchReplacementEntry.delete(0,'end')
            self.BatchReplacementEntry.insert(0,'Enter the batch...')
            self.UpdateReplacementButton.state(['disabled'])
            self.ChartButtonRe.state(['disabled']) 
        else:
            Question1=Toplevel()
            Question1.iconbitmap(Logo)
            Question1.title("Delete Batches")
            Label=ttk.Label(Question1,text="\tWould you like to\ndelete batches or all of them?",
                            font=Font_tuple3,foreground="Red")
            Label.pack()
            LabelFrami1=ttk.Labelframe(Question1,)
            LabelFrami1.pack()
            
            DeleteAllButton1=ttk.Button(LabelFrami1,text="Delete ALL",image=self.DeleteAllImg,
                                       compound=tk.LEFT,command=self.deleteAllReplacementBatch)
            DeleteAllButton1.grid(row=0,column=0,padx=10,pady=20)
            
            DeleteelementButton1=ttk.Button(LabelFrami1,text="Delete batches",image=self.DeleteAllImg,
                                           compound=tk.LEFT,)
            DeleteelementButton1.grid(row=0,padx=10,column=1)
            '''Need to create functions for both buttons''' 
    
    def IssueTrackerUpdateFunction(self):
        global BATCHES_ISSUE
        IssueTrackerUpdateClass(BATCHES_ISSUE).Main()
        del BATCHES_ISSUE
        logging.error("(UPDATE) Issue Tracker is updated")
        BATCHES_ISSUE=dict()
        messagebox.showinfo("UPDATE","All entered batches have been updated!")
        self.UpdateReplacementButton.state(['disabled'])
        
    def ReplacementChartDrawer(self):
        x_axe=[i.split(' ') for i in BATCHES_ISSUE.keys()]
        for i in x_axe:
            i.insert(-1,"\n")
        x_axe=[' '.join(i) for i in x_axe]
        y_axe=[i for i in BATCHES_ISSUE.values()]
        plt.bar(x_axe,y_axe)
        plt.title("Number of Issues / Batch") 
        plt.xlabel('Batches')
        plt.ylabel("Numbers of issues")
        plt.show()      
        
    
    def __init__(self) -> None:    
        super().__init__()
        
        self.DeleteAllImg=ImageTk.PhotoImage(resize_my_img9)
        self.clicked= StringVar()
        self.SubmitImg=ImageTk.PhotoImage(resize_my_img3)
        self.DeleteImg=ImageTk.PhotoImage(resize_my_img4) 
        self.InventoryImg=ImageTk.PhotoImage(resize_my_img6)
        self.InventoryMangImg=ImageTk.PhotoImage(resize_my_img7)
        self.MiniImage=ImageTk.PhotoImage(resize_my_img8)
        self.StatusImg=ImageTk.PhotoImage(resize_my_img5)
        self.DataImgur=ImageTk.PhotoImage(resize_my_img10)
        self.InstrImg=ImageTk.PhotoImage(resize_my_img11)
        self.UpdateImgur=ImageTk.PhotoImage(resize_my_img12)
        self.ReplacementImg=ImageTk.PhotoImage(resize_my_img13)
        
        
        s=ttk.Style()
        s.configure("my.TButton",font=Font_tuple3)
        
        self.title('Issue/Inventory updater')
        self.iconbitmap(Logo)
        
        #self.LOGOImage=ImageTk.PhotoImage(resize_img)
        self.Inventorylabel=ttk.Label(self,image=self.InventoryMangImg)
        self.Inventorylabel.pack()
        
        #InventoryFrame:
        
        self.InventoryFrame=ttk.Labelframe(self,text="Fill Section",borderwidth=2)
        self.InventoryFrame.pack()
        
        #work inside Inventory Frame
        self.BatchEntry=ttk.Entry(self.InventoryFrame,width=25, font=Font_tuple3)
        self.BatchEntry.grid(row=0,column=0,padx=10,pady=10)
        self.BatchEntry.insert(0,"Enter the batch...")
        
        self.submitbatch=ttk.Button(self.InventoryFrame,text="Submit",image=self.SubmitImg,
                                    compound=tk.LEFT,style="my.TButton",command=lambda:[self.GetBatchFunction(),self.NameBatchescheck()])
        self.submitbatch.grid(row=0,column=1,padx=10)
        
        self.deletebatch=ttk.Button(self.InventoryFrame,text="Delete",image=self.DeleteImg, compound=tk.LEFT,
                                    state="disabled",style="my.TButton",command=self.DeleteBatchesFunction)
        self.deletebatch.grid(row=0,column=2,padx=2.5)
        
        self.MiniImageButton=ttk.Button(self.InventoryFrame,
                                        image=self.MiniImage,command=self.deleteEntry)
        
        self.MiniImageButton.grid(row=1,column=1,columnspan=2)
        
        self.dropbox=ttk.OptionMenu(self.InventoryFrame, self.clicked, *Names,
                                    style="my.TButton" )
        self.dropbox.config(width=25)
        self.clicked.set("Select your name...")
        self.dropbox.grid(row=2,column=0)
        
        
        self.submitname=ttk.Button(self.InventoryFrame,text="Submit",image=self.SubmitImg,compound=tk.LEFT,
                                   style="my.TButton",command=lambda:[self.NamegetterFunction(),self.NameBatchescheck()] )
        self.submitname.grid(row=2,column=1,padx=10)

        
        self.deletename=ttk.Button(self.InventoryFrame,text="Delete",image=self.DeleteImg,compound=tk.LEFT,
                                   state="disabled",style="my.TButton",command=self.Namedeletefunction )
        self.deletename.grid(row=2,column=2,padx=2.5)
        
        self.InventoryUpdate=ttk.Button(self.InventoryFrame,text="Update Inventory",image=self.InventoryImg,compound=tk.LEFT,
                                        state="disabled",style="my.TButton",command=self.UpdateInventoryFunction )
        self.InventoryUpdate.grid(row=3,columnspan=3,column=0,pady=5)
        
        self.StatusButton=ttk.Button(self.InventoryFrame,image=self.StatusImg,
                                     compound=tk.LEFT,state="disabled",command=self.statusinfo)
        self.StatusButton.grid(row=4,column=0)
        
        self.ChartButton=ttk.Button(self.InventoryFrame,image=self.DataImgur,
                                    compound=tk.LEFT,state="!disabled",command=self.GetChartFunc)
        self.ChartButton.grid(row=4,column=1)
        
        self.InstrButton=ttk.Button(self.InventoryFrame,image=self.InstrImg,
                                    compound=tk.LEFT,command=self.InstructionFunction)
        self.InstrButton.grid(row=4,column=2)
        
        
        
        '''                 -------Replacement updater-------           '''
        self.ReplacementIcon=ttk.Label(self,image=self.UpdateImgur,compound=tk.LEFT)
        self.ReplacementIcon.pack()
        
        self.ReplacementFrame=ttk.LabelFrame(self,text="File Section")
        self.ReplacementFrame.pack()
        
        self.BatchReplacementEntry=ttk.Entry(self.ReplacementFrame,width=25, font=Font_tuple3)
        self.BatchReplacementEntry.grid(row=0,column=0,padx=10,pady=10)
        self.BatchReplacementEntry.insert(0,"Enter the batch...")
        
        self.submitbatchReplacement=ttk.Button(self.ReplacementFrame,text="Submit",image=self.SubmitImg,
                                    compound=tk.LEFT,style="my.TButton",command=lambda:[self.GetReplacementBatch(),self.Enablebutton()])
        self.submitbatchReplacement.grid(row=0,column=1,padx=10)
        
        self.deletebatchreplacement=ttk.Button(self.ReplacementFrame,text="Delete",image=self.DeleteImg, compound=tk.LEFT,
                                    state="disabled",style="my.TButton",command=self.DeleteReplacementBatchfunc)
        self.deletebatchreplacement.grid(row=0,column=2,padx=2.5)
        
        self.UpdateReplacementButton=ttk.Button(self.ReplacementFrame,text="Update Issue Tracker",
                                                image=self.ReplacementImg, compound=tk.LEFT,
                                                state="disabled",style="my.TButton",command=self.IssueTrackerUpdateFunction)
        self.UpdateReplacementButton.grid(row=1,column=0,columnspan=3,pady=5)
        
        self.StatusButtonRe=ttk.Button(self.ReplacementFrame,image=self.StatusImg,
                                     compound=tk.LEFT,state="disabled",)
        self.StatusButtonRe.grid(row=2,column=0)
        
        self.ChartButtonRe=ttk.Button(self.ReplacementFrame,image=self.DataImgur,
                                      compound=tk.LEFT,state="disabled",command=self.ReplacementChartDrawer)
        self.ChartButtonRe.grid(row=2,column=1)
        
        self.InstrButtonRe=ttk.Button(self.ReplacementFrame,image=self.InstrImg,
                                    compound=tk.LEFT,command=self.ReplacementInst)
        self.InstrButtonRe.grid(row=2,column=2)
        
        
        
        
        
if __name__=="__main__":
    App=IssueInventoryApp()
    App.mainloop()
    
'''
-Work on the delete button for the replacements
-Need to probably insert a detection 
-Gotta add Logs


'''