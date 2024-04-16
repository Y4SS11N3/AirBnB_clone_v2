<center> <h1>HBNB - The Console & MySQL Integration</h1> </center>

This repository contains the initial and advanced stages of a student project to build a clone of the AirBnB website. The initial stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions. The advanced stage introduces MySQL integration, transitioning from file storage to a more robust database storage system, allowing for complex data manipulation and management.

---

<center><h3>Repository Contents by Project Task</h3> </center>

| Tasks | Files | Description |
| ----- | ----- | ----------- |
| 0: Authors/README File | [AUTHORS](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/AUTHORS) | Project authors |
| 1: Pep8 | N/A | All code is pep8 compliant |
| 2: Unit Testing | [/tests](https://github.com/Y4SS11N3/AirBnB_clone/tree/dev/tests) | All class-defining modules are unit tested |
| 3: Make BaseModel | [/models/base_model.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/base_model.py) | Defines a parent class to be inherited by all model classes |
| 4: Update BaseModel w/ kwargs | [/models/base_model.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/base_model.py) | Add functionality to recreate an instance of a class from a dictionary representation |
| 5: Create FileStorage class | [/models/engine/file_storage.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/engine/file_storage.py), [/models/__init__.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/__init__.py), [/models/base_model.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/base_model.py) | Defines a class to manage persistent file storage system |
| 6: Console 0.0.1 | [console.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/console.py) | Add basic functionality to console program, allowing it to quit, handle empty lines and ^D |
| 7: Console 0.1 | [console.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/console.py) | Update the console with methods allowing the user to create, destroy, show, and update stored data |
| 8: Create User class | [console.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/console.py), [/models/engine/file_storage.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/engine/file_storage.py), [/models/user.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/user.py) | Dynamically implements a user class |
| 9: More Classes | [/models/user.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/user.py), [/models/place.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/place.py), [/models/city.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/city.py), [/models/amenity.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/amenity.py), [/models/state.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/state.py), [/models/review.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/review.py) | Dynamically implements more classes |
| 10: Console 1.0 | [console.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/console.py), [/models/engine/file_storage.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/engine/file_storage.py) | Update the console and file storage system to work dynamically with all classes update file storage |
| 11: MySQL setup development | [setup_mysql_dev.sql](#) | Script that prepares a MySQL server for the project |
| 12: MySQL setup test | [setup_mysql_test.sql](#) | Script that prepares a MySQL server for testing |
| 13: Delete object | [/models/engine/file_storage.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/engine/file_storage.py), [/models/engine/db_storage.py](#) | Update FileStorage and DBStorage to handle object deletion |
| 14: DBStorage - States and Cities | [/models/state.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/state.py), [/models/city.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/city.py), [/models/engine/db_storage.py](#) | Link states and cities to the MySQL database |
| 15: DBStorage - User | [/models/user.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/user.py), [/models/engine/db_storage.py](#) | Link users to the MySQL database |
| 16: DBStorage - Place | [/models/place.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/place.py), [/models/engine/db_storage.py](#) | Link places to the MySQL database |
| 17: DBStorage - Review | [/models/review.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/review.py), [/models/engine/db_storage.py](#) | Link reviews to the MySQL database |
| 18: DBStorage - Amenity | [/models/amenity.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/amenity.py), [/models/place.py](https://github.com/Y4SS11N3/AirBnB_clone/blob/dev/models/place.py), [/models/engine/db_storage.py](#) | Many-to-Many relationship between places and amenities |
<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

2. Change into the directory of the cloned repository:
   ```
   cd AirBnB_clone_v2
   ```

3. If you wish to use the MySQL storage system, ensure that MySQL is installed and running on your system. Then, execute the provided setup scripts to prepare your MySQL server:
   ```
   cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
   cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
   ```
   Enter your MySQL root password when prompted. These scripts will create the `hbnb_dev_db` and `hbnb_test_db` databases along with the `hbnb_dev` and `hbnb_test` users, respectively.

4. To start the console in file storage mode, run:
   ```
   /AirBnB_clone_v2$ ./console.py
   ```
   To start the console in database storage mode, set the `HBNB_TYPE_STORAGE` environment variable to `db` and provide the MySQL connection parameters:
   ```
   /AirBnB_clone_v2$ HBNB_TYPE_STORAGE=db HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db ./console.py
   ```

5. When the console is run, the following prompt should appear:
   ```
   (hbnb)
   ```
   This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

6. You can create, show, destroy, update, and list objects using the console commands. For example, to create a new `State` object with the name "California" in database storage mode, you would use:
   ```
   (hbnb) create State name="California"
   ```
   To list all `State` objects, use:
   ```
   (hbnb) all State
   ```
   To directly interact with the MySQL database and confirm the creation of the state, you can use MySQL commands:
   ```
   echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
   ```
   Enter your MySQL `hbnb_dev` password when prompted.

7. To exit the console, type `quit` or press `Ctrl-D`.

##### Commands
* `create` - Creates an instance based on given class. With MySQL integration, this command can also take parameters to set attributes upon creation. For example:
  ```
  create State name="California"
  ```
  This will create a new `State` instance with the name "California" and store it in the MySQL database if the storage type is set to `db`.

* `destroy` - Destroys an object based on class and UUID. In the case of MySQL storage, this will remove the record from the database.

* `show` - Shows an object based on class and UUID. If using MySQL, it retrieves the object from the database.

* `all` - Shows all objects the program has access to, or all objects of a given class. With MySQL, this command will query the database for all records of the specified class.

* `update` - Updates existing attributes of an object based on class name and UUID. For MySQL storage, this command will update the corresponding record in the database.

* `quit` - Exits the program (EOF will as well).

With the introduction of MySQL as a storage option, the console now interacts with a relational database to perform CRUD operations. The commands have been adapted to support both FileStorage and DBStorage systems, allowing for seamless switching between the two storage engines using the `HBNB_TYPE_STORAGE` environment variable.

To use the MySQL storage engine, ensure the following environment variables are set:
- `HBNB_MYSQL_USER`: MySQL username
- `HBNB_MYSQL_PWD`: MySQL password
- `HBNB_MYSQL_HOST`: MySQL host (usually localhost)
- `HBNB_MYSQL_DB`: MySQL database name
- `HBNB_TYPE_STORAGE`: Set to `db` to use MySQL

For example, to start the console with MySQL storage, you would run:
```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
```

When using the MySQL storage engine, you can directly interact with the database to confirm the changes made through the console commands. For instance, after creating a new state, you can use the following MySQL command to verify the record:
```
echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
```

##### Alternative Syntax
Users are able to issue a number of console commands using an alternative syntax, which is particularly useful when interacting with the MySQL database. This syntax allows for more direct manipulation of objects stored in the database.

Usage: `<class_name>.<command>([<id>][name_arg value_arg]|[kwargs]])`

This advanced syntax is implemented for the following commands:

- `all` - Shows all objects the program has access to, or all objects of a given class. This can be particularly useful for quickly querying the database for all instances of a specific class.

- `count` - Returns the number of object instances by class. This command is useful for getting a quick count of how many records exist in the database for a given class.

- `show` - Shows an object based on class and UUID. This command is used to retrieve a specific object from the database using its class name and unique identifier.

- `destroy` - Destroys an object based on class and UUID. This command allows for the deletion of a specific object from the database.

- `update` - Updates existing attributes of an object based on class name and UUID. This command is used to modify the attributes of an existing object in the database.

For example, to update a `User` object's name attribute, you could use the following command:
```
User.update("1234-5678-9012", "name", "John Doe")
```

Or, to create a new `State` with a name "California" directly in the database, you could use:
```
State.create("name=\"California\"")
```

These commands provide a powerful interface for managing the objects within the AirBnB clone project, allowing for direct interaction with the underlying MySQL database through the console.

Remember, when using the MySQL storage engine, ensure that the `HBNB_TYPE_STORAGE` environment variable is set to `db` and that the MySQL server is properly configured as described in the setup instructions.

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

<h3>MySQL Database Interaction Examples</h3>

###### State creation:
```
$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
```
```
$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
```
```
$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
```

###### City creation:
```
$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
```
```
$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)}]
(hbnb)
```
```
$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
```

###### User creation:
```
$ echo 'create User email="john@example.com" password="johnpwd" first_name="John" last_name="Doe"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) e97b2352-6eb9-4e58-aed8-2f0341b4fe77
(hbnb)
```
```
$ echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) [[User] (e97b2352-6eb9-4e58-aed8-2f0341b4fe77) {'id': 'e97b2352-6eb9-4e58-aed8-2f0341b4fe77', 'created_at': datetime.datetime(2024, 4, 15, 23, 52, 22), 'updated_at': datetime.datetime(2024, 4, 15, 23, 52, 22), 'email': 'john@example.com', 'first_name': 'John', 'last_name': 'Doe', 'password': 'johnpwd'}]
(hbnb)
```
```
$ echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: e97b2352-6eb9-4e58-aed8-2f0341b4fe77
created_at: 2024-04-15 23:52:22
updated_at: 2024-04-15 23:52:22
     email: john@example.com
  password: johnpwd
first_name: John
 last_name: Doe
```

These examples demonstrate how to interact with the MySQL database using the console for creating and querying State, City, and User objects. Each example includes the command line input and the expected output, providing a clear guide for users on how to use the AirBnB clone project with the MySQL storage engine.
