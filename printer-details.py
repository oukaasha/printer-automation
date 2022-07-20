import win32print
from win32con import *

# A List containing the system printers
all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]

print('\n\n####### --- PRINTERS --- #######')
print(all_printers)
print('####### --- PRINTERS --- #######\n\n')

DC_CONSTANTS = [
    DC_BINNAMES, DC_BINS, DC_COLLATE, DC_COLORDEVICE, DC_COPIES, DC_DRIVER,
    DC_DUPLEX, DC_ENUMRESOLUTIONS, DC_EXTRA, DC_FIELDS,
    DC_FILEDEPENDENCIES, DC_MAXEXTENT, DC_MEDIAREADY, DC_MEDIATYPENAMES,
    DC_MEDIATYPES, DC_MINEXTENT, DC_ORIENTATION, DC_NUP, DC_PAPERNAMES,
    DC_PAPERS, DC_PAPERSIZE, DC_PERSONALITY, DC_PRINTERMEM, DC_PRINTRATE, DC_PRINTRATEPPM,
    DC_PRINTRATEUNIT, DC_SIZE, DC_STAPLE, DC_TRUETYPE, DC_VERSION,
]

printer_to_be_used = all_printers[2]

def DC_INFO(constant):
    for a_global in globals().keys():
        if a_global.startswith("DC_") and globals().get(a_global) == constant:
            return a_global
    return "DC_UNKNOWN"


print('\n\n####### --- PRINTER DETAILS --- #######')
for constant in DC_CONSTANTS:
    try:
        x = win32print.DeviceCapabilities(printer_to_be_used, '', constant)
        print("\t", DC_INFO(constant), x)
    except:
        pass

printer = win32print.OpenPrinter(printer_to_be_used, {"DesiredAccess":win32print.PRINTER_ALL_ACCESS})

P_DEV_MODE_KEYS = [
    'BitsPerPel', 'Collate', 'Color', 'Copies', 
    'DefaultSource', 'DeviceName', 'DisplayFixedOutput', 
    'DisplayFlags', 'DisplayFrequency', 'DisplayOrientation', 
    'DitherType', 'DriverExtra', 'DriverVersion', 
    'Duplex', 'Fields', 'FormName', 'ICMIntent', 'ICMMethod', 
    'LogPixels', 'MediaType', 'Nup', 'Orientation', 
    'PanningHeight', 'PanningWidth', 'PaperLength', 'PaperSize', 
    'PaperWidth', 'PelsHeight', 'PelsWidth', 'Position_x', 
    'Position_y', 'PrintQuality', 'Reserved1', 'Reserved2', 
    'Scale', 'Size', 'SpecVersion', 'TTOption', 'YResolution'
]

properties = win32print.GetPrinter(printer, 2)
# print(dir(properties['pDevMode']))
# print(properties)

for key in P_DEV_MODE_KEYS:
    try:
        val = getattr(properties['pDevMode'], key)
        print("\t", key, val)
    except:
        pass

print('####### --- PRINTER DETAILS --- #######\n\n')