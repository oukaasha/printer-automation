import win32print

# A List containing the system printers
all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]

print('\n\n####### --- PRINTERS --- #######')
print(all_printers)
print('####### --- PRINTERS --- #######\n\n')

printer_to_be_used = all_printers[2]

printer = win32print.OpenPrinter(printer_to_be_used, {"DesiredAccess":win32print.PRINTER_ALL_ACCESS})

print(win32print.EnumJobs(printer, 0, -1, 2))
# print(win32print.GetJob(printer, 7, 1))

win32print.ClosePrinter(printer)