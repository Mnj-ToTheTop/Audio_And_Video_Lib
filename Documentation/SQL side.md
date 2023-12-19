# TABLES AND FIELDS

There are a total of 5 tables in the database namely, Audio, Video, Customer Employee and Requested.

1. Audio table: The audio table has two attributes or columns.
     1. Name: Contains the title of the audio. The data type of this attribute is VARCHAR type.
     2. File: Contains the audio file in the form of binary data which is encoded in the form of ASCII characters. The data type of this attribute is LONGBLOB.

2. Video table: The video table has two attributes or columns.
     1. Name: Contains the title of the video in the form of a string. The data type of this attribute is VARCHAR type.
     2. File: Contains the video file in the form of binary data which is encoded in the form of ASCII characters. The data type of this attribute is LONGBLOB.

3. Customer table: The table contains the information of the customers of the Library. This information is accessed when a customer logs into the library. This contains three attributes.
     1. Name: Contains the name of the customer in the form of a string. The data type of this attribute is VARCHAR.
     2. User_Id: Contains the user id of the customer in the form of a string. The data type of this attribute is VARCHAR. This is the primary key for the table, thus each user id is unique.
     3. Password: Contains the password of the customer’s account. The data type of this attribute is VARCHAR.

          Name  | User_Id  | Password  
        ------------- | -------------  | ---------
        Manjara  | MnjRaj   | D3cade
        Calry  | Nyc#Shadown   | V1#Shadown
        Ruby  | RED@gem  | super#St
  
4. Employee table: This table contains information on the employees of the library. This information is accessed when an employee logs in the library system. It contains three attributes.
      1. Name: Stores the name of the employee in the form of a string. The data type of the attribute is VARCHAR.
      2. Emp_ID: Stores the employee id of each employee which is unique to individual employees. It is the primary key of the table and the attribute’s data type is VARCHAR.
      3. Password: Contains the password of each employee in the form of a string. The data type of this output is VARCHAR.
         
     Name  | Emp_Id  | Password  
    ------------- | -------------  | ---------  
    Kenya  | Ken@Lif  | pizza@PIZZA  
		

5. Requested table: This table stores information about the content requested by the customers. This table has two attributes.
      1. Name: Stores the title of the content in the form of a string. The data type of this attribute is VARCHAR.
      2. Media: Stores the file type of the content requested by the customers in the form of a string. The data type of the field is VARCHAR.
      3. Cust_Name: Stores the name of the customer that requests the content
