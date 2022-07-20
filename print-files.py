import os
import win32print
import win32api
from win32con import *



# A List containing the system printers
all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]

print('\n\n####### --- PRINTERS --- #######')
print(all_printers)
print('####### --- PRINTERS --- #######\n\n')

printer_to_be_used = all_printers[2]

printer = win32print.OpenPrinter(printer_to_be_used, {"DesiredAccess":win32print.PRINTER_ALL_ACCESS})

properties = win32print.GetPrinter(printer, 2)
properties['pDevMode'].Duplex = DMDUP_VERTICAL
properties['pDevMode'].PaperSize = DMPAPER_A4

win32print.SetPrinter(printer, 2, properties, 0)

win32print.SetDefaultPrinter(printer_to_be_used)


# win32print.StartPagePrinter(printer)
# jobid = win32print.StartDocPrinter(printer, 1, ['postcard-maker-code.pdf', None, None])
# print(jobid)
# print(win32print.GetJob(printer, jobid, 1))
# win32print.EndDocPrinter(printer)


INPUTDIR = './to-be-processed'

input_filenames = [f for f in os.listdir(INPUTDIR) if f.endswith('.pdf')]

for input_file in input_filenames:
    print('Printing: ', input_file)
    win32api.ShellExecute(0, "print", os.path.join(INPUTDIR, input_file), None,  ".",  0)
    try:
        print('JobId: ', win32print.EnumJobs(printer, 0, -1, 2))
    except:
        pass


win32print.ClosePrinter(printer)