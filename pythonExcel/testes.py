from openpyxl import load_workbook

wb = load_workbook('material_externo.xlsx')

valor = 6

print(wb['VLS'][f'B{valor}'].value)
