from flask import Flask

# deklarasi variabel app untuk menampung atau membangun Object Class Framework Flask
app    = Flask(__name__)

# deklarasi variable config untuk mengatur konfigurasi dasar dari flask
# port untuk port app flask saat di jalankan
# debug untuk mengaktivkan mode debug jika bernilai benar (True)
config = {
    'port': 5000,
    'debug': True
}

"""
 deklarasi rute / atau root path web flask
 dengan method Get
 http://localhost:port/
 Method atau Function Index
 Fungsi yang digunakan ketika 
 menjalankan atau mengakses route /
 return index string
"""
@app.route("/", methods=['GET'])
def index():
    index = "Selamat Datang Di KPM - Membuat ChatBot"
    return index

if __name__=="__main__":
    try:
        app.run(**config)
    except ImportError:
        print("install : pip install -i requirements.txt") 