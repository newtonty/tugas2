# Bagan Request Client ke Web

![Bagan Django](https://user-images.githubusercontent.com/113079090/221418715-3aa8565f-b71f-454a-80ef-5ae1b23e9145.png)

1. Client akan melakukan request terhadap URL.
2. URL akan memilih View.
3. View akan melakukan QuerySet terhadap Model.
4. Model akan melakukan transaksi data dengan Database.
5. Model akan merespon data sesuai dengan data yang ada pada Database.
6. View akan memilih template HTML yang berada pada directory Template.
7. Template akan menampilkan halaman HTML di Web.

## Penggunaan Virtual Environment

Virtual Environment akan memastikan bahwa versi dari sebuah library pada suatu project tidak akan berubah apabila kita melakukan update pada library yang sama di project lainnya. Jika Virtual Environment tidak digunakan, library perlu didowngrade untuk mengerjakan project lainnya (dan perlu diupgrade saat mengerjakan project yang lain)

## Instruksi Penggunaan

1. Membuat App Study Tracker dengan python manage.py startapp study_tracker.
2. Menambahkan app study_tracker pada INSTALLED_APPS di settings, register App di apps dan URL settings.
![image](https://user-images.githubusercontent.com/113079090/221419850-70722ca8-9213-406b-94cf-5d3e9c2f1b94.png)
![image](https://user-images.githubusercontent.com/113079090/221419878-008187ab-cb79-49aa-ba60-5aa66922d9d6.png)
![image](https://user-images.githubusercontent.com/113079090/221419700-37ca0180-99dc-47de-911e-c9e91ad8557c.png)
![image](https://user-images.githubusercontent.com/113079090/221419724-e5666fc5-5508-4dc8-a286-8d897d1aacc7.png)

3. Membuat class Assignment pada models.py di study_tracker. Register models pada admin.py.
![image](https://user-images.githubusercontent.com/113079090/221419756-a1a99fe2-ace0-4269-808c-6c6acb6e6a2c.png)
![image](https://user-images.githubusercontent.com/113079090/221419896-f46dfa39-2bbf-4b00-a1a2-bc8fd13ed299.png)

4. Mengambil data pada object Assignment melalui views.py
![image](https://user-images.githubusercontent.com/113079090/221420001-ede8cec1-628e-4af5-9479-261abf05017d.png)

Source:
Kelas Terbuka. (2018). Tutorial Django 1.11 Bahasa Indonesia. Retrieved from https://youtube.com/playlist?list=PLZS-MHyEIRo6p_RwsWntxMO5QAqIHHHld
