import pandas as pd

# 假設文件名稱是已知的，例如 'students.txt' 和 'majors.txt'
students_file = './inputtable/students.txt'
majors_file = './inputtable/majors.txt'

# 用來存放所有的表格文件
# 以表格名稱為 key，表格 DataFrame 為 value
tables = {}

# tool function
# 宣告一個可以將table仔入tables的函數
def load_table(tableName, table):
    global tables
    tables[tableName] = table
     


def read_table(file_path):
    """
    讀取指定路徑的表格文件並返回 DataFrame
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def print_tables():
    # 打印出目前在tables中的表格
    global tables
    print("\nTables:")
    if len(tables) == 0:
        print("No tables found")
        return
    
    for table_name in tables:
        print(f"\nTable Name: {table_name}\n{'-' * 40}")
        if tables[table_name].empty:
            print(f"Table {table_name} is empty")
        else:
            print(tables[table_name])
        print(f"{'-' * 40}\n")


def print_table(table_name):
    # 選擇一個表格並打印出來
    global tables
    if table_name in tables:
        print(f"\nTable Name: {table_name}\n{'-' * 40}")
        if tables[table_name].empty:
            print(f"Table {table_name} is empty")
        else:
            print(tables[table_name])
        print(f"{'-' * 40}\n")
    else:
        print(f"Table {table_name} not found")

    
def print_options():
    """
    打印基本的操作選項
    """
    print("\n**************************")
    print("operations:")
    print("* 0. quit")
    print("* 1. select")
    print("* 2. project")
    print("* 3. rename")
    print("* 4. cartesian product")
    print("* 5. union")
    print("* 6. difference")
    print("* 7. Set Intersection")
    print("**************************")
    print("tools:")
    print("* 8. print all tables")
    print("* 9. print a table")   
    print("*10. delete a table")
    print("**************************\n")


def concatenate_tables(table1, table2):
    global tables  # 讓func 知道在用的是全域的tables
    result = []  # 結果
    # 每一行都加入到結果中
    for index, row in tables[table1].iterrows():  
        result.append(row.to_dict())  
    for index, row in tables[table2].iterrows():  
        result.append(row.to_dict())  
    new_table = pd.DataFrame(result)  
    return new_table  

def merge_tables(table1, table2):
    global tables # 讓func 知道在用的是全域的tables
    result = [] # 結果
    # 比對兩個表格的每一行，如果相同就加入到結果中
    for index1, row1 in tables[table1].iterrows():
        for index2, row2 in tables[table2].iterrows():
            if row1.equals(row2):
                result.append(row1.to_dict())
    new_table = pd.DataFrame(result)
    return new_table

def left_join_tables(table1, table2):
    # 這種實現方式叫做左外連接
    # 可以用merge函數來實現

    global tables # 讓func 知道在用的是全域的tables
    result = [] # 結果
    # 比對兩個表格的每一行，如果不同就加入到結果中
    for index1, row1 in tables[table1].iterrows():
        match_found = False
        for index2, row2 in tables[table2].iterrows():
            if row1.equals(row2):
                match_found = True
                break
        if not match_found:
            result.append(row1.to_dict())
    new_table = pd.DataFrame(result)
    return new_table

# instruction function
def select(table, condition):
    # select 函數的實現
    global tables
    if table in tables:
        try:
            return tables[table].query(condition)
        except Exception as e:
            print(f"Error executing select: {e}")
    else:
        print(f"Table {table} not found")

def project(table, columns):
    # project 函數的實現
    global tables
    new_table = None
    if table in tables:
        try:
            new_table = tables[table][columns.split(", ")]
            # 找出重複的行
            # new_table = new_table.drop_duplicates()
        except Exception as e:
            print(f"Error executing project: {e}")
    else:
        print(f"Table {table} not found")

def product(table1, table2):
    # cartesian product 函數的實現
    global tables
    new_table = None
    result = []
    if table1 in tables and table2 in tables:
        try:
            # 這裡使用了兩個for迴圈，來將兩個表格的每一行進行組合
            for index1, row1 in tables[table1].iterrows():
                for index2, row2 in tables[table2].iterrows():
                    # 將兩行合併成一行
                    new_row = {**row1, **row2}
                    result.append(new_row)
            # 將結果存入new_table
            new_table = pd.DataFrame(result)
            return new_table
        except Exception as e:
            print(f"Error executing product: {e}")
    else:
        print(f"Table {table1} or {table2} not found")


def union(table1, table2):
    # union 函數的實現
    global tables
    new_table = None
    if table1 in tables and table2 in tables:
        try:
            new_table = concatenate_tables(table1, table2)
            # 找出重複的行
            new_table = new_table.drop_duplicates()
            return new_table
        except Exception as e:
            print(f"Error executing union: {e}")
    else:
        print(f"Table {table1} or {table2} not found")

def difference(table1, table2):
    # difference 函數的實現
    global tables
    new_table = None
    if table1 in tables and table2 in tables:
        try:
            new_table = left_join_tables(table1, table2)
            return new_table
        except Exception as e:
            print(f"Error executing difference: {e}")
    else:
        print(f"Table {table1} or {table2} not found")


def intersection(table1, table2):
    # intersection 函數的實現
    global tables
    new_table = None
    if table1 in tables and table2 in tables:
        try:
            # 這裡使用了merge_tables函數，來找出兩個表格中相同的行
            new_table = merge_tables(table1, table2)
            return new_table
        except Exception as e:
            print(f"Error executing intersection: {e}")
    else:
        print(f"Table {table1} or {table2} not found")



def run_menu(students, majors):
    while True:
        print_options()
        choice = input("請輸入你的選擇：")
        if choice == '0':
            return
        elif choice == '1':
            # select
            # 輸入條件，然後選擇表格
            condition = input("Enter the condition for selection (e.g., major_name == 'Computer Science'): ")
            table = input("Enter the table to select from (students or majors): ")
            retsult = input("Enter new table name to save the result: ")
            # 執行select函數
            new_table = select(table, condition)
            if new_table is not None:
                # 將結果存入tables
                load_table(retsult, new_table)
        elif choice == '2':
            # project
            # 輸入要保留的欄位，然後選擇表格
            columns = input("Enter the columns to project (e.g., student_id, name): ")
            table = input("Enter the table to project from (students or majors): ")
            retsult = input("Enter new table name to save the result: ")
            # 執行project函數
            new_table = project(table, columns)
            if new_table is not None:
                # 將結果存入tables
                load_table(retsult, new_table)
        elif choice == '3':
            # rename
            # 輸入要重命名的table 跟新的名字
            old_table = input("Enter the table to rename: ")
            new_table = input("Enter the new name for the table: ")
            if old_table in tables:
                tables[new_table] = tables[old_table]
        elif choice == '4':
            # cartesian product
            # 輸入兩個表格，然後執行cartesian product
            table1 = input("Enter the first table for the product (e.g., students): ")
            table2 = input("Enter the second table for the product (e.g., majors): ")
            retsult = input("Enter new table name to save the result: ")
            new_table = product(table1, table2)
            if new_table is not None:
                # 將結果存入tables
                load_table(retsult, new_table)
        elif choice == '5':
            # print("You selected 'union'")
            # 輸入兩個表格，然後執行union
            table1 = input("Enter the first table for the union (e.g., studentNo1): ")
            table2 = input("Enter the second table for the union (e.g., studentsNo2): ")
            retsult = input("Enter new table name to save the result: ")
            new_table = union(table1, table2)
            if new_table is not None:
                # 將結果存入tables
                load_table(retsult, new_table)
        elif choice == '6':
            # print("You selected 'difference'")
            # 輸入兩個表格，然後執行difference
            table1 = input("輸入要被刪減的表格 (e.g., studentNo1): ")
            table2 = input("輸入想要刪減的內容 (e.g., studentNo2): ")
            retsult = input("Enter new table name to save the result: ")
            new_table = difference(table1, table2)
            if new_table is not None:
                # 將結果存入tables
                load_table(retsult, new_table)
        elif choice == '7':
            # print("You selected 'Set Intersection'")
            table1 = input("Enter the first table for the intersection (e.g., studentNo1): ")
            table2 = input("Enter the second table for the intersection (e.g., studentNo2): ")
            retsult = input("Enter new table name to save the result: ")
            new_table = intersection(table1, table2)
            if new_table is not None:
                # 將結果存入tables
                load_table(retsult, new_table)
        elif choice == '8':
            print_tables()
        elif choice == '9':
            table_name = input("Enter the name of the table to print: ")
            print_table(table_name)
        elif choice == '10':
            table_name = input("Enter the name of the table to delete: ")
            if table_name in tables:
                del tables[table_name]
            else:
                print(f"Table {table_name} not found")
        else:
            print("Invalid choice. Please try again.")



def main():
    students = read_table(students_file)
    majors = read_table(majors_file)
    load_table('students', students)
    load_table('majors', majors)


    # 這裡先印出來給使用者看看，以便後續的操作
    if students is not None and majors is not None:
        print_tables()
    else:
        print("Error : please give input tables")
    
    # 做一個基礎的輸出選項
    # 讓使用者選擇要使用的指令
    run_menu(students_file, majors_file)
    print("Goodbye!")


if __name__ == "__main__":
    main()
