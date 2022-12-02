## Printer Automation

**make-pdf.py** file takes pdf files from `input`, puts a unique qr code on the top right of every page, and then puts the result in `to-be-processed` (optional)

**print-files.py** takes pdf files from `to-be-processed` one by one, and starts printing them based on the value in printer list

**printer-details.py** lists down all the printers in the system, and displays the details for one of them based on this variable: `printer_to_be_used`

**printer-jobs.py** lists down all the printers in the system, and displays the jobs for one of them based on this variable: `printer_to_be_used`

Main file is this one: **printer-notification.py** takes pdf files from `to-be-processed` and prints them using the printer defined in variable `printer_to_be_used` and puts the printed file in `processed`.

Meanwhile, it also displays all the required information of a printer, like JOB_STATUS and other valuable information
