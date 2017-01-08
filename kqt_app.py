
import tkinter as tk
import sqlite3 as lite 


class kqt_app(tk.Frame):
	def __init__(self,parent):
		tk.Frame.__init__(self,parent)
		self.parent = parent
		self.initialize()
		self.db_connect()
		self.data_pull=[]
		
	#Connect to the Snohomish DB and pull 25 records to fill first instance of the Results table
	def db_connect(self):
		self.con = lite.connect('adj_snohomish.db')
		self.cur = self.con.cursor()
		self.data_pull = self.cur.execute('SELECT * FROM MAIN LIMIT 25')
	
	#Function to Delete items in the List Box
	def listbox_del(self, event=None):
		self.results_listbox.delete(tk.ANCHOR)
	
	#Function for putting search results into the listbox
	def insert_data(self):
		self.results_listbox.delete(0,tk.END)
		for data in self.data_pull:
			self.results_listbox.insert(tk.END, data)
			
	#GENERATE SEARCH FUNCTION:
	def generate_search(self):
		self.city_var = str(self.entry_city.get())
		self.type_var = str(self.entry_type.get())
		self.zip_var = str(self.entry_zip.get())
		self.value_var = str(self.entry_value.get())
		self.name_var = str(self.entry_name.get())
		
		#USING THE ALL PLACE HOLDER WILL DO A SELECT ALL QUERY
		if self.city_var == self.type_var == self.zip_var == self.value_var == self.name_var == 'ALL':
			self.data_pull = self.cur.execute('SELECT * FROM MAIN LIMIT 25')
			self.insert_data()
	
		#IF ONLY CITY IS ENTERED  
		if self.city_var != 'ALL':
			self.data_pull = self.cur.execute('SELECT * FROM MAIN WHERE SitusCity = (?) LIMIT 25', (self.city_var,))
			self.insert_data()
		
		#IF ONLY TYPE IS ENTERED
		if self.type_var != 'ALL':
			self.data_pull = self.cur.execute('SELECT * FROM MAIN WHERE USE = (?) LIMIT 25', (self.type_var,))
			self.insert_data()
		
		#IF ONLY ZIP IS ENTERED
		if self.zip_var != 'ALL':
			self.data_pull = self.cur.execute('SELECT * FROM MAIN WHERE ZipCode = (?) LIMIT 25', (self.zip_var,))
			self.insert_data()
		
		#IF ONLY VALUE IS ENTERED
		if self.value_var != 'ALL':
			self.data_pull = self.cur.execute('SELECT * FROM MAIN WHERE MKTTL < (?) LIMIT 25', (self.value_var,))
			self.insert_data()
		
		#IF ONLY CITY,VALUE IS ENTERED
		 #?????
		
		
		
	#********CREATES THE GUI********************	
	def initialize(self):
		self.grid()
		
		######CREATE SEARCH QUERY PANEL (LabelFrame)
		self.search_frame = tk.LabelFrame(self,text='Search field',padx=5,pady=5, background = 'dark grey')
		self.search_frame.pack(side = tk.TOP, fill=tk.BOTH, padx=5, pady=1, ipadx=5, ipady=1)
		
		######INSERT WIDGETS INTO SEARCH QUERY PANEL
		
		#City FRAME
		self.city_area = tk.Frame(self.search_frame, background='pink', padx=5,pady=5)
		self.city_area.grid(row=1,column=1)
		#INSERT WIDGETS
		self.label_city = tk.Label(self.city_area, text = 'City', background='pink')
		self.label_city.grid(row=1,column=1)
		#
		self.entry_city = tk.Spinbox(self.city_area, values=('ALL','EVERETT','MARYSVILLE','LYNNWOOD','BOTHELL','SNOHOMISH','EDMONDS','ARLINGTON','LAKE STEVENS','STANDWOOD','MONROE','MUKILTEO','MOUNTLAKE TERRACE', 'MILL CREEK', 'GRANITE FALLS', 'SULTAN', 'GOLD BAR', 'BRIER', 'SNOHOMISH COUNTY', 'WOODINVILLE', 'TULALIP', 'DARRINGTON'))
		self.entry_city.grid(row=2,column=1)
		
		#Property Type FRAME
		self.property_area = tk.Frame(self.search_frame, background='pink',padx=5,pady=5)
		self.property_area.grid(row=1,column=2)
		##INSERT WIDGETS 
		self.label_type = tk.Label(self.property_area, text ='Property Type', background='pink')
		self.label_type.grid(row=1,column=1)
		#
		self.entry_type = tk.Spinbox(self.property_area, width = 45, values=('ALL','111 Single Family Residence - Detached', '910 Undeveloped (Vacant) Land', '143 Single Family Residence Condominium Multiple','118 Manufactured Home (Owned Site)',' Single Family Residence Condominium Detached', '119 Manufactured Home (Mobile Home Park)','119 Vacant Site Mobile Home Park', '122 Two Family Residence (Duplex)', '145 Condominium Conversion','142 Single Family Residence Condominium Common Wall', '144 Single Family Residence Conominium Project', 'Four Family Residence (Flour Plex)', '198 Vacation Cabin'))
		self.entry_type.grid(row=2,column=1)
			
		#Zip Code FRAME
		self.zip_area = tk.Frame(self.search_frame, background='pink',padx=5,pady=5)
		self.zip_area.grid(row=1,column=3)
		#INSERT WIDGETS
		self.label_zip = tk.Label(self.zip_area, text ='Zip Code', background = 'pink')
		self.label_zip.grid(row=1,column=1)
		#
		self.entry_zip = tk.Spinbox(self.zip_area, values=('ALL','98012','98223','98208','98270','98258','98290'))
		self.entry_zip.grid(row=2,column=1)
		
		#Assessor Value FRAME
		self.value_area = tk.Frame(self.search_frame, background='pink',padx=5,pady=5)
		self.value_area.grid(row=1,column=4)
		#INSERT WIDGETS
		self.label_value = tk.Label(self.value_area, text ='Assessor Value (MAXIMUM)', background='pink')
		self.label_value.grid(row=1,column=1)
		#
		self.entry_value = tk.Spinbox(self.value_area, values=('ALL'))
		self.entry_value.grid(row=2,column=1)
		
		#LastName Value FRAME
		self.name_area = tk.Frame(self.search_frame, background = 'pink',padx=5,pady=5)
		self.name_area.grid(row=1,column=5)
		#INSERT WIDGETS
		self.label_name = tk.Label(self.name_area, text = 'Last Name', background='pink')
		self.label_name.grid(row=1,column=1)
		#
		self.entry_name = tk.Spinbox(self.name_area, values=('ALL'))
		self.entry_name.grid(row=2,column=1)
		
		#StreetName Value FRAME
		self.street_area = tk.Frame(self.search_frame, background = 'pink', padx=5,pady=5)
		self.street_area.grid(row=1,column=6)
		#INSERT WIDGETS
		self.label_street = tk.Label(self.street_area, text = 'Street Name', background='pink')
		self.label_street.grid(row=1,column=1)
		#
		self.entry_street = tk.Spinbox(self.street_area, values=('ALL'))
		self.entry_street.grid(row=2,column=1)
		
		
		#SEARCH BUTTON
		self.search_button = tk.Button(self.search_frame, text='Search', command=self.generate_search, background='white')
		self.search_button.grid(row=2,column=6)
		
		######RESULTS PANEL#########
		self.results_panel = tk.LabelFrame(self, text = 'Results', padx=3,pady=3, background = 'grey')
		self.results_panel.pack(side=tk.BOTTOM, fill=tk.BOTH,padx = 5, pady = 5, ipadx=5, ipady=5 )
		
		##LISTBOX INSIDE RESULTS PANEL
		self.results_listbox = tk.Listbox(self.results_panel, height = 25)
		self.results_listbox.pack(fill=tk.BOTH, expand = 1)
		self.results_listbox.bind('<Control-d>', self.listbox_del)
		
		##Generate Letter Button
		self.generate_letter_button = tk.Button(self.results_panel, text = 'Generate Letters', command= lambda: print(self.results_listbox.get(0,tk.END)))
		self.generate_letter_button.pack(side=tk.BOTTOM)
		

if __name__ =='__main__':
	app=kqt_app(None)
	app.mainloop()
	
