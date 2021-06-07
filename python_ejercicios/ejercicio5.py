## ABRIR UN EXCEL EN PYTHON CON LIBRERIA XLRD (SIN EXITO)


import xlrd

file_path = ("C:\\Users\\Nacho\\Documents\\tabla_imc.xlsx")

open_file = xlrd.open_workbook(file_path)

sheet = open_file.sheet_by_name("Hoja1")


# num_rows = sheet.nrows
# num_cols = sheet.ncols

# print("nº de filas: " + str(num_rows))
# print("nº de columnas: " + str(num_cols))

# print(type(num_rows))

print(open_file.nsheets)

print(open_file.sheet_names())

cell = sheet.cell(0, 0)
print(cell)

cell = sheet.cell(6,1)
print (cell)

print (cell.value)



