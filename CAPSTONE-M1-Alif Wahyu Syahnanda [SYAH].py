# CAPSTONE PROJECT 1 Alif Wahyu Syahnanda (SYAH)
# HEALTH FACILITY PROGRAMS

from tabulate import tabulate
import regex as re
import sys
import datetime

# ------------------------------------- INTEGRATION BLOCK CODE -------------------------------------
# LANDING PAGE
def mainmenu():
    print('''
        --------------------------------------------------
        🚑🏥💉Welcome to Jakarta National Hospital🚑🏥💉
        --------------------------------------------------
                            MAIN MENU
        Log in as
            1. Patients-User
            2. Employee
            3. Exit
            ''')

# LANDING PAGE FUNCTION
def landingpage():
    mainmenu() 
    while True:
        try:
            optionlogin = int(input('LANDING PAGE COMMAND\nEnter the Main Menu Number: '))
            if optionlogin == 1:
                patientmenu()
            elif optionlogin == 2:
                emplogin()
            elif optionlogin == 3:
                print('Thank you for coming ! Stay Healthy and Speedy Recovery !')
                print('Your Health is Our Priority')
                sys.exit()
            else :
                print('Please Choose Log in as! (only type 1-3)')
        except ValueError:
            print('LANDING PAGE HINT: WRONG INPUT !\nINPUT LOG IN AS AGAIN !')

# ------------------------------------- DATABASE BLOCK CODE -------------------------------------    
# EMPLOYEE ID-PASSWORD
empdata =  {
    'Fulan': 'FU1234',
    'Boi': 'B1234',
    'Mutia': 'MU1234'
}

# PATIENTS DATA
patient = [
    {'REG_NUMBER':'JNHREG01','Name': 'Komeng','Birthdate':'01/02/1984','Age': 40,'Gender':'M','Illness':'Cataracts','Telephone':'082177551233','Address': 'Pasar Minggu, South Jakarta'},
    {'REG_NUMBER':'JNHREG02','Name': 'Astra','Birthdate':'01/02/1984','Age': 20,'Gender':'F','Illness':'Tifus','Telephone':'087857733588','Address': 'Mampang, South Jakarta'},
    {'REG_NUMBER':'JNHREG03','Name': 'Buya','Birthdate':'01/02/1984','Age': 56,'Gender':'M','Illness':'Asthma','Telephone':'087857733588','Address': 'Pejaten, South Jakarta'},
    {'REG_NUMBER':'JNHREG04','Name': 'Sarinah','Birthdate':'01/02/2007','Age': 17,'Gender':'F','Illness':'Misaligned teeth','Telephone':'0877806751900','Address': 'Pejaten, South Jakarta'}
]

# DOCTORS SCHEDULE DATA
doctors = [
    {'Doc_ID':'DOC01','Doctor Name':'dr. IRWAN SAIFUL, M.KES','Specialist':'General','Day':'Mon - Fri','Time':'08:00 - 13:00'},
    {'Doc_ID':'DOC02','Doctor Name':'drg. RAYA JULIANTI','Specialist':'Dental','Day':'Wed - Fri','Time':'15:30 - 19:00'},
    {'Doc_ID':'DOC03','Doctor Name':'dr. INDAH, Sp.PD','Specialist':'Internist','Day':'Mon - Fri','Time':'07:00 - 11:00'},
    {'Doc_ID':'DOC04','Doctor Name':'dr. ISA ANSARI, Sp.M','Specialist':'Ophthalmologist ','Day':'Mon, Wed, Fri','Time':'14:30 - 16:00'}
]


# ------------------------------------- VALIDATION BLOCK CODE -------------------------------------
# LETTER VALIDATION
def validalpha(label,info):
    while True:
       print(info)
       inputan = input(label)
       if re.fullmatch("[a-zA-Z]+", inputan):
            inputan = inputan
            return inputan
       elif re.fullmatch("[\w]+", inputan):
            print("INVALID INPUT")
       else:
            print('CANT EMPTY VALUE')

# NUMBER VALIDATION
def validnum(label,info):
    while True:
        print(info)
        number = input(label)
        if re.fullmatch("[\d]+", number):
            number = int(number)
            return number
        elif re.fullmatch("[\w]+", number):
            print("INVALID INPUT")
        else:
            print('CANT EMPTY VALUE')

# BIRTHDATE VALIDATION
def input_birthdate():
    while True:
        try:
            date = input('Input Your Birthdate \n(format DD/MM/YYYY) \t: ')
            birthdate = datetime.datetime.strptime(date,'%d/%m/%Y').date()
            return birthdate
        except ValueError:
            print('Invalid Input !, Use Format DD/MM/YYYY')



# ------------------------------------- READ FEATURES BLOCK CODE -------------------------------------
# READ PATIENTS DATA
def patients_data():
    table1 = tabulate(patient, headers='keys', tablefmt='pretty')
    print(table1)
    print(f'Number of patients  : {len(patient)}')
    print('''NOTE
GENDER : M (MALE) / F (FEMALE)          
    ''')

# READ DOCTORS SCHEDULE DATA
def docschedule():
    table2 = tabulate(doctors, headers='keys', tablefmt='pretty')
    print(table2)
    print(f'Available Doctors : {len(doctors)}')

# ------------------------------------- CREATE FEATURES BLOCK CODE -------------------------------------
# CREATE/ADD FUNCTION DATA PATIENTS
def create_data_patient():
    while True:
        print('\nFill Patient New Data Below >\n')     
        regnewid = input('Input New REG_NUMBER JNHREGxx \n(fill xx with continuing numbers): \t').upper()
        newname= validalpha('Enter New Patient Name \t: ','\nLETTERS ONLY')
        newbirthdate= input_birthdate()
        newage = validnum('Input Patient Age \t: ','\nNUMBERS ONLY')
        newgender = (validalpha('Enter Gender \t: ','\nChoose M/F Only').upper())
        newill = validalpha('Input New Initial Diagnosis \t: ','\nLETTERS ONLY')
        newtel = validnum('Input Patient Telephone \t: ','\nNUMBERS ONLY')
        newaddr = input('Enter New Address \t: ')
        newdatapatient = {'REG_NUMBER': regnewid,'Name': newname,'Birthdate': newbirthdate,'Age': newage,'Gender':newgender,'Illness':newill,'Telephone':newtel,'Address': newaddr}
        while True:
            confirm = input(f'Confirm input Data? REG_NUMBER:{regnewid},Name:{newname}, Birthdate:{newbirthdate},Age: {newage},Gender:{newgender},Illness:{newill},Telephone:{newtel},Address:{newaddr}(Y/N) \t: ')
            try:
                if confirm.upper() == 'Y':
                    patient.append(newdatapatient)
                    print('\nNew Patient Successfully Added !\n')
                    patients_data()
                    break
                elif confirm.upper() == 'N':
                    print('Thank you, Have a Nice Day !')
                    break
            except:
                print('INVALID INPUT')
        while True:
            confirm2 = input('Do You Want Add More Data? (Y/N)').capitalize()
            if confirm2 == 'Y':
                create_data_patient()
            elif confirm2 == 'N':
                print('Thank you !')
                return emp_submenu1()
            else:
                print('Choose Y/N!')



# CREATE/ADD FUNCTION DATA DOCTORS
def create_data_doc():
    while True:
        print('\nFill Out Data Doctor Below >\n')  
        newiddoc= input('EXAMPLE > DOC01\nEnter New Doctors ID DOCxx \t: ').upper()  
        newnamedoc= input('Enter Doctor Name \t: ')
        newspecialist= validalpha('Input Specialization \t: ','\nLETTERS ONLY').capitalize()
        newworkday = input('Input Work Day \t: ')
        newtime = input('Input Work Time \t: ')
        newdatadoc = { 'Doc_ID':newiddoc,'Doctor Name':newnamedoc,'Specialist':newspecialist,'Day':newworkday,'Time':newtime}
        while True:
            confirm = input(f'Confirm input Data? Doctor Doc_ID:{newiddoc},Name:{newnamedoc},Specialist:{newspecialist},Day:{newworkday},Time:{newtime}(Y/N) \t: ')
            try:
                if confirm.upper() == 'Y':
                    doctors.append(newdatadoc)
                    print('\nNew Doctor Successfully Added !\n')
                    docschedule()
                    break
                elif confirm.upper() == 'N':
                    print('Thank you, Have a Nice Day !')
                    break
            except:
                print('INVALID INPUT')
        while True:
            confirm2 = input('Do You Want Add More Data? (Y/N)').capitalize()
            if confirm2 == 'Y':
                create_data_doc()
            elif confirm2 == 'N':
                print('Thank you !')
                return emp_submenu2()
            else:
                print('Choose Y/N !')

   
# ------------------------------------- UPDATE FEATURES BLOCK CODE -------------------------------------
# EDIT/UPDATE FUNCTION PATIENTS ILLNESS DATA
def updatedatpat():
    print(f'''
    🖊️Select the Data You Want to Update :
        1. Disease/Illness
        2. Phone Number
        3. Update Address
        4. Back to Sub Menu
    ''')
    inputan = int(input('Choose Number \t: '))
    while True:
        try:
            if inputan == 1:
                patients_data()
                old_ill = input("Enter the disease to be updated \t: ")
                new_ill = input("Type 'back' for cancel\nEnter New Disease \t: ")

                for item in patient:
                    if item['Illness'] == old_ill:
                        item['Illness'] = new_ill
                        patients_data()
                        print("Data Successfully Updated!")
                        break
                    elif old_ill == 'back':
                        return updatedatpat()
                    else:
                        print('Data not Found')
            elif inputan == 2:
                patients_data()
                old_pn = input("Enter the Phone Number to be updated \t: ")
                new_pn = input("Type 'back' for cancel\nEnter New Phone Number \t: ")

                for item in patient:
                    if item['Telephone'] == old_pn:
                        item['Telephone'] = new_pn
                        patients_data()
                        print("Data Successfully Updated!")
                        break
                    elif old_pn == 'back':
                        return updatedatpat()
                    else:
                        print('Data not Found')
            elif inputan == 3:
                patients_data()
                old_add = input("Insert current address \t: ")
                new_add = input("Type 'back' for cancel\nInsert New Address \t: ")

                for item in patient:
                    if item['Address'] == old_add :
                        item['Address'] = new_add
                        patients_data()
                        print("Data Successfully Updated!")
                        break
                    elif old_add == 'back':
                        return updatedatpat()
                    else:
                        print('Data not Found')
            elif inputan == 4:
                emp_submenu1()
            else:
                print('\nINVALID INPUT > CHOOSE 1 - 4\n')
        except ValueError:
            print('\nINVALID INPUT : NUMBERS ONLY\n')


# EDIT/UPDATE FUNCTION DOCTORS DATA
def updatedatadoc():
    print(f'''
    Select the Data in Doctor You Want to Update :
        1. Practice Day
        2. Time Practice
        3. Back to Sub Menu
    ''')
    inputan = int(input('Choose Number \t: '))
    while True:
        try:
            if inputan == 1:
                docschedule()
                old_pd = input("Enter the Day to be updated \t: ")
                new_pd = input("Type 'back' for cancel\nEnter New Practice Day \t: ")

                for item in patient:
                    if item['Illness'] == old_pd:
                        item['Illness'] = new_pd
                        docschedule()
                        print("Data Successfully Updated!")
                        break
                    elif old_pd == 'back':
                        updatedatadoc()
                    else:
                        print('Data not Found')
            elif inputan == 2:
                docschedule()
                old_tp = input("Enter Time to be updated \t: ")
                new_tp = input("Type 'back' for cancel\nEnter New Time \t: ")

                for item in patient:
                    if item['Telephone'] == old_tp:
                        item['Telephone'] = new_tp
                        docschedule()
                        print("Data Successfully Updated!")
                        break
                    elif old_tp == 'back':
                        updatedatadoc()
                    else:
                        print('Data not Found')        
            elif inputan == 3:
                emp_submenu2()
            else:
                print('\nINVALID INPUT > CHOOSE 1 - 3\n')
        except ValueError:
            print('\nINVALID INPUT : NUMBERS ONLY\n')

# ------------------------------------- DELETE FEATURES BLOCK CODE -------------------------------------

# DELETE FUNCTION PATIENTS DATA
def deleteEntry():
    while True:
        choice = int(input("Select the database you want to delete:\n 1. Patients Data\n 2. Back to Sub-Menu\n Enter your choice: "))
        try:
            if choice == 1:
                patients_data()
                entryID = input("Masukkan Nomor Registrasi Pasien yang ingin dihapus: ")
                entryID = entryID.upper()
                # Find the index of the entry with the given REG_NUMBER
                index_to_delete = None
                for idx, entry in enumerate(patient):
                    if entry['REG_NUMBER'] == entryID:
                        index_to_delete = idx
                        break
                if index_to_delete is not None:
                    del patient[index_to_delete]
                    print(f"Patient data with REG_NUMBER : {entryID} was successfully deleted.\n Check Updated Data in View All Patients Data")
                    break
                else:
                    print("Registration number not found. Please try again.")
            elif choice == 2:
                emp_submenu1()
            else:
                print("Your input was incorrect, please try again.")
        except ValueError:
            print('\nINVALID INPUT : NUMBERS ONLY\n')
    emp_submenu1()


# DELETE FUNCTION DOCTORS DATA
def deleteEntrydoc():
    while True:
        choice = int(input("Select the database you want to delete:\n 1. Doctors Data\n 2. Back to Sub-Menu\n Enter your choice: "))
        try:
            if choice == 1:
                docschedule()
                entryID = input("Enter the Doctor ID Number that you want to delete: ")
                entryID = entryID.upper()
                # Find the index of the entry with the given Doc_ID
                index_to_delete = None
                for idx, entry in enumerate(doctors):
                    if entry['Doc_ID'] == entryID:
                        index_to_delete = idx
                        break
                if index_to_delete is not None:
                    del patient[index_to_delete]
                    print(f"Doctor data with Doc_ID : {entryID} was successfully deleted.\n Check Updated Data in View All Doctors Schedule")
                    break
                else:
                    print("ID number not found. Please try again.")
            elif choice == 2:
                emp_submenu2()
            else:
                print("Input anda salah, silahkan coba lagi.")
        except ValueError:
            print('\nINVALID INPUT : NUMBERS ONLY\n')
    emp_submenu2()

# ------------------------------------- SEARCH FEATURE BLOCK CODE ------------------------------------
#MENU SEARCH PATIENTS DATABASE
def search_datapat():
    print(f'''

🍳SEARCHING PATIENTS DATA
          
    1. REG_NUMBER
    2. Patient Name
    3. Back to Sub Menu

''')
    while True:
        select_no = int(input('Choose a number in searching patients data \t: '))
        try:
            if select_no == 1:
                searchinpat('REG_NUMBER')
                break
            elif select_no == 2:
                searchinpat('Name')
            elif select_no == 3:
                return emp_submenu1()
            else: 
                print('INVALID INPUT')
        except:
            print('\nINVALID INPUT : NUMBERS ONLY\n')

#SEARCH FUNCTION FOR PATIENTS DATABASE
def searchinpat(atribute):
    global patient, found, item, results
    keys = ['REG_NUMBER','Name','Birthdate','Age','Gender','Illness','Telephone','Address']
    found = 'not found'
    results = []
    while True:
        search = input(f'\nInput {atribute} you want to search \t: ')
        search = search
        if not search.strip():
            print(">>>Input Can not Empty<<<")
            continue
        try:
            for item in patient:
                atribute_search = item[atribute]
                if re.search(search, atribute_search):
                    found = 'found'
                    results.append(item)
            if found == 'found':
                for result in results:
                    print('<<Result search patients data>>')
                    print(tabulate([result.values()], headers=keys, tablefmt='pretty'))
                break
            else:
                print('>>>Data Not Found<<<')
                break
        except:
            print(f'>>>{atribute} is invalid<<<')
        break
    

#MENU SEARCH DOCTORS DATABASE
def search_datadoc():
    print(f'''

🍳SEARCHING DOCTORS DATA
          
    1. Specialization
    2. Day Available
    3. Back to Sub Menu (ONLY FOR PATIENTS)

''')
    while True:
        select_no = int(input('Choose a number in searching doctors data \t: '))
        
        if select_no == 1:
            searchindoc('Specialist')
        elif select_no == 2:
            searchindoc('Day')
        elif select_no == 3:
            patientmenu()
        elif select_no == 9:
            emp_submenu2()
        else: 
            print('INVALID INPUT')
#SEARCH FUNCTION FOR DOCTORS DATABASE
def searchindoc(atribute):
    global doctors, found, item, results
    keys = ['Doc_ID','Doctor Name','Specialist','Day','Time']
    found = 'not found'
    results = []
    while True:
        search = input(f'\nInput {atribute} you want to search \t: ')
        search = search
        if not search.strip():
            print(">>>Input Can not Empty<<<")
            continue
        try:
            for item in doctors:
                atribute_search = item[atribute]
                if re.search(search, atribute_search):
                    found = 'found'
                    results.append(item)
                
                    print('>>>Data Not Found<<<')
            if found == 'found':
                for result in results:
                    print('<<Result search doctors data>>')
                    print(tabulate([result.values()], headers=keys, tablefmt='pretty'))
                break
            elif search == 'back' :
                return emp_submenu2()
            else:
                print('>>>Data Not Found<<<')
                break
        except:
            print(f'>>>{atribute} is invalid<<<')
        break
            

# -------------------------------------- SORT FILTER BLOCK CODE --------------------------------------

#SORT FILTER MENU PATIENTS
def sortfilmenupat():
    print('''
    ⌛SORT & FILTER PATIENTS DATABASE MENU⌛
        1. SORT DATA
        2. FILTER DATA
        3. Back to Sub Menu
''')
    what = int(input('What You Want to Do? \t: '))
    while True:
        try:
            if what == 1:
                sort_datapat()
            elif what == 2:
                filter_datapat(patient)
            elif what == 3:
                emp_submenu1()
                break
            else:
                print('Try Input Again')
        except ValueError:
            print('INVALID INPUT')
            break

# FUNCTION SORT DATA PATIENTS
def sort_datapat():
    global patient
    print('''
            Choose Sorted Data based on Alphabet:
            1. Age
            2. Gender
            3. Illness/Disease
            4. Address
            5. Back to Sub Menu''')
    sort = input('Select to sort data \t: ')
    while True:
        if sort == '5':
            sortfilmenupat()
        elif sort in ['1','2','3','4']:
            try:
                if sort == '1':
                    patient = sorted(patient, key = lambda x : x['Age'])
                    patients_data()
                    break
                elif sort == '2':
                    patient = sorted(patient, key = lambda x : x['Gender'])
                    patients_data()
                    break
                elif sort == '3':
                    patient = sorted(patient, key = lambda x : x['Illness'])
                    patients_data()
                    break
                elif sort == '4':
                    patient = sorted(patient, key = lambda x : x['Address'])
                    patients_data()
                    break
            except:
                print('Select Digit Only 1-5 !')
        else:
            print('Enter options 1 through 4 or 5 to return to the previous menu!')

# FUNCTION FILTER DATA
def filter_dict(patient, key, value):
    filtered_list = []
    for item in patient:
        if item.get(key) == value:
            filtered_list.append(item)
    if not filtered_list:
        print('Data not found!')
    return filtered_list

# FUNCTION MENU FILTER DATA PATIENTS
def filter_datapat(patient):
    print('''
          Please choose the filter you want to use:
            1. Gender
            2. Illness
            3. Back to Sort Filter Menu
            ''')
    opsi = input('Enter the number: ')
    try:
        if opsi == '3':
            sortfilmenupat()
        elif opsi in ['1', '2']:
            if opsi == '1':
                Gender = input('Input Filter M/F \t: ').upper()
                key = 'Gender'
                value = Gender
                result = filter_dict(patient, key, value)
                tablefil1 = tabulate(result, headers='keys', tablefmt='pretty')
                print(tablefil1)
            elif opsi == '2':
                Illness = input('Enter Disease Filter \t: ').title()
                key = 'Illness'
                value = Illness
                result = filter_dict(patient, key, value)
                tablefil2 = tabulate(result, headers='keys', tablefmt='pretty')
                print(tablefil2)
            else:
                print('Enter options 1 through 2 or 3 to return to the previous menu!')
        else:
            print('Enter options 1 through 2 or 3 to return to the previous menu!')
    except Exception as e:
        print('Error:', e)



# ------------------------------------- PATIENTS MENU BLOCK CODE -------------------------------------
#PATIENTS LANDING MENU
def patientmenu():
    usernamein = input('Enter Your Name: ')
    while True:
        print(f'''

📌Hi {usernamein.capitalize()}, Welcome to Your Beloved Hospital !🚑🏥💉

VISITOR & PATIENTS PAGE
1. Check Doctor Schedule 👩‍⚕️👨‍⚕️
2. Find Doctor
3. Log in page
4. Exit     
        ''')
        userpage = int(input('Enter the menu number: '))
        if userpage == 1:
            docschedule()
        elif userpage == 2:  
            search_datadoc()
        elif userpage == 3:
            landingpage()
        elif userpage == 4:
            sys.exit()

# ------------------------------------- EMPLOYEES MENU BLOCK CODE -------------------------------------

#EMPLOYEE LOG IN MENU
def emplogin():
    print(f'> LOG IN - ENTER YOUR EMPLOYEE ID & PASSWORD')
    empid = input('Enter Your Employee ID: ').capitalize()
    password = input('Enter Your Password: ').upper()
    if empid in empdata and password == empdata[empid]:
        print('LOG IN SUCCESSFULL')
        emp_mainmenu()
    else:
        print('Wrong Username or Password !')
        return(emplogin())

#EMPLOYEE LANDING PAGE MENU
def emp_mainmenu():
    while True:
        print(f'''
    -----------------------------------------
        Hi You, Have a Good Day at Work ! 
    -----------------------------------------

        Employee Main Menu
        1. All Patient Database
        2. Doctor Schedule Database
        3. Back to Log in Menu
        4. Exit
              
        ''')
        option_empmenu = int(input('Enter the menu number: '))
        if option_empmenu == 1:
            emp_submenu1()
        elif option_empmenu == 2:
            emp_submenu2()
        elif option_empmenu == 3:
            landingpage()
        elif option_empmenu == 4:
            sys.exit()
        else:
            print('INVALID INPUT!')

#EMPLOYEE SUB-MENU 1 - Accessing All Patients Database
def emp_submenu1():
    print('Jakarta National Hospital - Patients Database')
    print(f'''
        SUB MENU Patients Database
        1. View All Patients Data
        2. Add Patients Data
        3. Update Patients Data
        4. Find-Search Patients Data
        5. Sort & Filter Patients Data
        6. Delete Patients Data
        7. Back to Employee Main Menu
        8. Exit  
        ''')
    opt_empsubmenu1 = int(input('Enter the menu number: '))
    while True:
        try:
            if opt_empsubmenu1 == 1:
                patients_data()
                break
            elif opt_empsubmenu1 == 2:
                create_data_patient()
            elif opt_empsubmenu1 == 3:
                updatedatpat()
            elif opt_empsubmenu1 == 4:
                search_datapat()
            elif opt_empsubmenu1 == 5:
                sortfilmenupat()
            elif opt_empsubmenu1 == 6:
                deleteEntry()
            elif opt_empsubmenu1 == 7:
                emp_mainmenu()
            elif opt_empsubmenu1 == 8:
                sys.exit()
            else:
                print('INVALID INPUT!')
                return(emp_submenu1)
        except ValueError:
            print('WRONG INPUT! CHOOSE ONLY SUB MENU NUMBER!')
            break

    
#EMPLOYEE SUB-MENU 2 - Accessing Doctor Database
def emp_submenu2():
    print('Jakarta National Hospital - Doctors Database')
    print(f'''
        SUB MENU Doctor Database
        1. View All Doctor Schedule
        2. Add Doctor Schedule
        3. Update Doctor Schedule
        4. Find-Search Doctor Schedule
        5. Delete Doctor Schedule
        6. Back to Employee Main Menu
        7. Exit  
        ''')
    opt_empsubmenu2 = int(input('Enter the menu number: '))
    while True:
        try:
            if opt_empsubmenu2 == 1:
                docschedule()
                break
            elif opt_empsubmenu2 == 2:
                create_data_doc()
            elif opt_empsubmenu2 == 3:
                updatedatadoc()
            elif opt_empsubmenu2 == 4:
                print('INPUT 9 : GO BACK TO SUB MENU FOR EMPLOYEES')
                search_datadoc()
            elif opt_empsubmenu2 == 5:
                deleteEntrydoc()
            elif opt_empsubmenu2 == 6:
                emp_mainmenu()
            elif opt_empsubmenu2 == 7:
                sys.exit()
            else:
                print('INVALID INPUT!')
                return(emp_submenu2())
        except ValueError:
            landingpage()
            print(f'Sorry, Try Again')


# CALL TO RUN
landingpage()