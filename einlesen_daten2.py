import csv
from datetime import datetime
import Sitec_dataset

'''csv_files = ["bb_handeingabe.csv", "bb_messwert.csv",
             "be_handeingabe.csv", "be_messwert.csv",
             "br_handeingabe.csv", "br_messwert.csv",
             "kt_handeingabe.csv", "kt_messwert.csv",
             "li_handeingabe.csv", "li_messwert.csv",
             "ne_handeingabe.csv", "ne_messwert.csv",
             "pa_handeingabe.csv", "pa_messwert.csv"]'''

#read sitec file
sitec_header = ["Anlage", "Label", "Akz", "Einheit", "Messart", "Maxima", "Minima"]
sitec_file = open("sitec_funkt_einh.csv", newline='')
sitec_data = csv.DictReader(sitec_file, delimiter=',', fieldnames=sitec_header)

#create sitec class
sitec = Sitec_dataset.SitecDataset()

for line in sitec_data:
    sitec.appendData(line["Akz"],line["Label"],line["Minima"],line["Maxima"],0)

hand_header = ['Akz', 'Datum', 'Wert']
hand_file = open("bb_handeingabe.csv", newline='')
hand_data = csv.DictReader(hand_file, delimiter=',', fieldnames=hand_header)

for line in hand_data:
    datum = datetime.strptime(line["Datum"], '%Y-%m-%d %H:%M:%S')
    datum_timestamp = datum.timestamp()
    akz_list = sitec.get_akz()
    find_akz_index = akz_list.index(line["Akz"])
    latestTimestamp_list = sitec.get_latestTimestamp()
    if latestTimestamp_list[find_akz_index] < datum_timestamp:
        sitec.updateTimestampByIndex(find_akz_index, datum_timestamp)

print(sitec.get_akz()[554])
print(sitec.get_latestTimestamp()[554])
